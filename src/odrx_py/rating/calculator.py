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

    def calculate_rating(self) -> float:
        if not self.mods:
            return 0.0

        # --- Extract speed multiplier ---
        speed_multiplier = 1.0
        for mod in self.mods:
            if mod.get("acronym") == Mods.CustomSpeed:
                settings = mod.get("settings", {})
                speed_multiplier = settings.get("rateMultiplier", 1.0)
                break

        # --- Validate mods ---
        if not any(mod.get("acronym") == Mods.Relax for mod in self.mods):
            return None

        if any(
            mod.get("acronym")
            in [Mods.AutoPilot, Mods.DifficultyAdjust, Mods.WindDown, Mods.WindUp]
            for mod in self.mods
        ):
            return None

        beatmap = Beatmap(path=str(self.beatmap))
        overall_difficulty = beatmap.od - 4

        applied = False

        # --- Apply speed mods correctly ---
        if speed_multiplier != 1.0:
            for i, mod in enumerate(self.mods):
                acronym = mod.get("acronym")

                if acronym == Mods.DoubleTime:
                    self.mods[i] = {
                        "acronym": "DT",
                        "settings": {"speed_change": 1.5 * speed_multiplier},
                    }
                    applied = True
                    break

                elif acronym == Mods.HalfTime:
                    self.mods[i] = {
                        "acronym": "HT",
                        "settings": {"speed_change": 0.75 * speed_multiplier},
                    }
                    applied = True
                    break

                elif acronym == Mods.NightCore:
                    self.mods[i] = {
                        "acronym": "NC",
                        "settings": {"speed_change": 1.5 * speed_multiplier},
                    }
                    applied = True
                    break

        calc = Difficulty(mods=self.mods)

        if not applied and speed_multiplier != 1.0:
            calc.set_clock_rate(speed_multiplier)

        # --- Base OD adjustments ---
        calc.set_od(overall_difficulty, od_with_mods=False)

        # --- Handle special mods ---
        for mod in self.mods:
            acronym = mod.get("acronym")

            if acronym == Mods.Precise:
                overall_difficulty += 4
                calc.set_od(overall_difficulty, od_with_mods=False)

            elif acronym == Mods.ShitMod:
                overall_difficulty = overall_difficulty / 2

                calc.set_ar(beatmap.ar - 0.5, ar_with_mods=True)
                calc.set_od(overall_difficulty, od_with_mods=False)
                calc.set_cs(beatmap.cs * 0.5, cs_with_mods=False)

        calc = calc.calculate(map=beatmap)

        return round(float(calc.stars), 2)
