import json
from typing import Optional

from ..enums import Mods


class ModHelper:
    def __init__(self, mods: Optional[dict] = None):
        self.mods = json.loads(mods) if mods else None

    @property
    def parse(self) -> str:
        if not self.mods:
            return Mods.NoMod

        parsed = []

        for mod in self.mods:
            try:
                mod_acronym = Mods(mod["acronym"])
            except ValueError:
                continue

            mod_settings = mod.get("settings")
            parsed_mod = mod_acronym if mod_acronym != Mods.ShitMod else "REZ"

            if mod_settings:
                match mod_acronym:
                    case Mods.CustomSpeed:
                        rate = mod_settings.get("rateMultiplier", 1.0)
                        parsed_mod = f"CS({rate}x)"
                    case Mods.DifficultyAdjust:
                        settings = ", ".join(
                            f"{k}: {v}" for k, v in mod_settings.items()
                        )
                        parsed_mod = f"DA({settings})"

            parsed.append(parsed_mod)

        return "".join(parsed)
