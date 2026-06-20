
from dataclasses import dataclass
from pathlib import Path

from rosu_pp_py import Beatmap, BeatmapAttributesBuilder, Difficulty

from ..enums import Mods


@dataclass
class BeatmapAttributes:
    stars: float
    max_combo: int
    ar: float
    od: float
    cs: float
    hp: float


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

    def calculate_rating(self) -> BeatmapAttributes | None:
        if not self.mods:
            return None

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

        # --- Strip CustomSpeed and apply speed mods correctly ---
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

        # --- Build shared Difficulty and BeatmapAttributesBuilder with same overrides ---
        calc  = Difficulty(mods=submit_mods)
        attrs = BeatmapAttributesBuilder(mods=submit_mods, map=beatmap)

        if not applied and speed_multiplier != 1.0:
            calc.set_clock_rate(speed_multiplier)
            attrs.set_clock_rate(speed_multiplier)

        # --- Base OD adjustments (difficulty calc only, not attrs builder) ---
        calc.set_od(overall_difficulty, False)

        # --- Handle special mods ---
        for mod in self.mods:
            acronym = self._get_acronym(mod)

            if acronym == Mods.Precise:
                overall_difficulty += 4
                calc.set_od(overall_difficulty, False)
                attrs.set_od(overall_difficulty, False)

            elif acronym == Mods.ShitMod:
                overall_difficulty /= 2
                calc.set_ar(beatmap.ar - 0.5, True)
                calc.set_od(overall_difficulty, False)
                calc.set_cs(beatmap.cs * 0.5, False)
                attrs.set_ar(beatmap.ar - 0.5, True)
                attrs.set_od(overall_difficulty, False)
                attrs.set_cs(beatmap.cs * 0.5, False)

        result     = calc.calculate(map=beatmap)
        bmap_attrs = attrs.build()

        return BeatmapAttributes(
            stars=result.stars,
            max_combo=result.max_combo,
            ar=result.ar,
            od=bmap_attrs.od,
            cs=bmap_attrs.cs,
            hp=result.hp,
        )
        
