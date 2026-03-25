from dataclasses import dataclass

@dataclass
class Beatmap:
    id: int
    set_id: int
    hash: str
    artist: str
    title: str
    version: str
    creator: str
    ar: int
    cs: int
    hp: int
    od: int
    mode: int
    stars: int
    status: int
    lenght: int
