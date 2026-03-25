import json
from typing import Optional

class ModHelper:
    def __init__(self, mods: Optional[dict] = None):
        self.mods = json.loads(mods)
    
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
    
def check_get_user_attrs(uid: int=None, username: str=None):
        if username is None and uid is None:
            raise Exception("Username or UID must be provided.")
        elif isinstance(username, str) is not True and uid is None:
            raise Exception("Username must be string.")
        if uid is None and username is None:
            raise Exception("UID must not be empty if from_username is False.")
        elif isinstance(uid, int) is not True and username is None:
            raise Exception("UID must be int.")