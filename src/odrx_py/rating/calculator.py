from pathlib import Path

from rosu_pp_py import Beatmap, Difficulty

from ..enums import Mods


class SRCalculator:
    def __init__(
        self,
        beatmap: Path,
        mods: list[dict] = None,
    ):
        if not beatmap.exists():
            raise FileNotFoundError(f"Beatmap file not found: {str(beatmap)}")
        self.beatmap = beatmap
        self.mods = mods or []

    def _get_acronym(self, mod: dict) -> str:
        return mod.get("acronym", "")

    def calculate_rating(self) -> Difficulty:
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
            return None

        if any(m in acronyms for m in (Mods.AutoPilot, Mods.DifficultyAdjust, Mods.WindDown, Mods.WindUp)):
            return None

        beatmap = Beatmap(path=str(self.beatmap))
        overall_difficulty = beatmap.od - 4

        # --- Strip CS mod and apply speed mods correctly (no mutation of self.mods) ---
        submit_mods = [mod for mod in self.mods if self._get_acronym(mod) != Mods.CustomSpeed]

        applied = False

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

        calc = Difficulty(mods=submit_mods)

        if not applied and speed_multiplier != 1.0:
            calc.set_clock_rate(speed_multiplier)

        # --- Base OD adjustments ---
        calc.set_od(overall_difficulty, od_with_mods=False)

        # --- Handle special mods ---
        for mod in self.mods:
            acronym = self._get_acronym(mod)

            if acronym == Mods.Precise:
                overall_difficulty += 4
                calc.set_od(overall_difficulty, od_with_mods=False)

            elif acronym == Mods.ShitMod:
                overall_difficulty /= 2
                calc.set_ar(beatmap.ar - 0.5, ar_with_mods=True)
                calc.set_od(overall_difficulty, od_with_mods=False)
                calc.set_cs(beatmap.cs * 0.5, cs_with_mods=False)

        result = calc.calculate(map=beatmap)

        return result
