from enum import IntEnum

class BeatmapStatus(IntEnum):
    Graveyard = -2
    Unsubmitted = -1
    Pending = 0
    Ranked = 1
    Approved = 2
    Qualified = 3
    Loved = 4
    Whitelisted = 5

    def __str__(self) -> str:
        return self.name.lower()

class BeatmapMode(IntEnum):
    Standard = 0
    Taiko = 1
    Catch = 2
    Mania = 3
    
    def __str__(self) -> str:
        return self.name.lower()