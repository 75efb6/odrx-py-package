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
    
def check_get_user_attrs(uid: int=None, username: str=None, from_username: bool=False):
        if from_username is not True and from_username is not False:
            raise Exception("from_username must be True or False")
        if username is None and from_username is True:
            raise Exception("Username must not be empty if from_username is True.")
        elif isinstance(username, str) is not True and from_username is True:
            raise Exception("Username must be string.")
        if uid is None and from_username is False:
            raise Exception("UID must not be empty if from_username is False.")
        elif isinstance(uid, int) is not True and from_username is False:
            raise Exception("UID must be int.")