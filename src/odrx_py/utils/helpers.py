import json
from typing import Optional


class ModHelper:
    def __init__(self, mods: Optional[dict] = None):
        self.mods = json.loads(mods) if mods else None

    @property
    def parse(self) -> str:
        if not self.mods:
            return "NM"

        parsed = []

        for mod in self.mods:
            match mod["acronym"]:
                case "CS":
                    mod = f"CS({mod["settings"]["rateMultiplier"]}x)"
                case "RE":
                    mod = "REZ"
                case "DA":
                    settings = []
                    for setting, value in mod["settings"].items():
                        settings.append(f"{setting}: {value}")
                    settings = ", ".join(settings)
                    mod = f"DA({settings})"
                case _:
                    mod = mod["acronym"]

            parsed.append(mod)

        return "".join(parsed)
