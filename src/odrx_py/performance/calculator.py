from pathlib import Path

from rosu_pp_py import Beatmap, BeatmapAttributesBuilder, Performance

from ..enums import Mods


class PPCalculator:
    def __init__(
        self,
        beatmap: Path,
        mods: list[dict] = None,
        n300: int = 0,
        n100: int = 0,
        n50: int = 0,
        misses: int = 0,
        combo: int = 0,
    ):
        if not beatmap.exists():
            raise FileNotFoundError(f"Beatmap file not found: {str(beatmap)}")
        self.beatmap = beatmap
        self.mods = mods or []
        self.n300 = n300
        self.n100 = n100
        self.n50 = n50
        self.misses = misses
        self.combo = combo

    def _get_acronym(self, mod: dict) -> str:
        return mod.get("acronym", "")

    def calculate_performance(self) -> float:
        if not self.mods:
            return 0.0

        acronyms = [self._get_acronym(m) for m in self.mods]

        # --- Extract speed multiplier ---
        speed_multiplier = 1.0
        for mod in self.mods:
            if self._get_acronym(mod) == Mods.CustomSpeed:
                speed_multiplier = mod.get("settings", {}).get("rateMultiplier", 1.0)
                break

        # --- Validate mods ---
        if Mods.Relax not in acronyms:
            return 0.0

        if any(m in acronyms for m in (Mods.AutoPilot, Mods.DifficultyAdjust, Mods.WindDown, Mods.WindUp)):
            return 0.0

        beatmap = Beatmap(path=str(self.beatmap))
        overall_difficulty = beatmap.od - 4

        # --- Strip CS mod before passing to rosu-pp-py ---
        submit_mods = [mod for mod in self.mods if self._get_acronym(mod) != Mods.CustomSpeed]

        applied = False

        # --- Apply speed mods correctly ---
        if speed_multiplier != 1.0:
            for i, mod in enumerate(submit_mods):
                acronym = self._get_acronym(mod)

                if acronym == Mods.DoubleTime:
                    submit_mods[i] = {"acronym": Mods.DoubleTime, "settings": {"speed_change": 1.5 * speed_multiplier}}
                    applied = True
                    break

                elif acronym == Mods.HalfTime:
                    submit_mods[i] = {"acronym": Mods.HalfTime, "settings": {"speed_change": 0.75 * speed_multiplier}}
                    applied = True
                    break

                elif acronym == Mods.NightCore:
                    submit_mods[i] = {"acronym": Mods.NightCore, "settings": {"speed_change": 1.5 * speed_multiplier}}
                    applied = True
                    break

        performance = Performance(mods=submit_mods)
        beatmap_attributes = BeatmapAttributesBuilder(mods=submit_mods, map=beatmap)

        if not applied and speed_multiplier != 1.0:
            performance.set_clock_rate(speed_multiplier)
            beatmap_attributes.set_clock_rate(speed_multiplier)

        # --- Base OD adjustments ---
        performance.set_od(overall_difficulty, od_with_mods=False)
        beatmap_attributes.set_od(overall_difficulty, od_with_mods=False)

        # --- Handle special mods ---
        for mod in self.mods:
            acronym = self._get_acronym(mod)

            if acronym == Mods.Precise:
                overall_difficulty += 4
                performance.set_od(overall_difficulty, od_with_mods=False)
                beatmap_attributes.set_od(overall_difficulty, od_with_mods=False)

            elif acronym == Mods.ShitMod:
                overall_difficulty = overall_difficulty / 2
                performance.set_ar(beatmap.ar - 0.5, ar_with_mods=True)
                performance.set_od(overall_difficulty, od_with_mods=False)
                performance.set_cs(beatmap.cs * 0.5, cs_with_mods=False)
                beatmap_attributes.set_ar(beatmap.ar - 0.5, ar_with_mods=True)
                beatmap_attributes.set_od(overall_difficulty, od_with_mods=False)
                beatmap_attributes.set_cs(beatmap.cs * 0.5, cs_with_mods=False)

        # --- Score data ---
        performance.set_n300(self.n300)
        performance.set_n100(self.n100)
        performance.set_n50(self.n50)
        performance.set_misses(self.misses)
        performance.set_combo(self.combo)

        result = performance.calculate(beatmap)
        attrs = beatmap_attributes.build()

        # --- AR bonus ---
        ar_bonus = 0.0
        if attrs.ar > 10.33:
            ar_bonus += 0.4 * (attrs.ar - 10.33)
        elif attrs.ar < 8.0:
            ar_bonus += 0.01 * (8.0 - attrs.ar)

        pp = result.pp * (1 + min(ar_bonus, ar_bonus * (beatmap.n_objects / 1000)))

        if pp >= 10000:
            return 0.0

        return round(float(pp), 2)