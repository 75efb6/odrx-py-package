from dataclasses import dataclass
from ..enums import BeatmapStatus


@dataclass
class Beatmap:
    id: int
    set_id: int
    hash: str
    artist: str
    title: str
    version: str
    creator: str
    ar: float
    cs: float
    hp: float
    od: float
    mode: int
    stars: float
    status: BeatmapStatus
    lenght: int
