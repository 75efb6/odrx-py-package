from dataclasses import dataclass

from objects.player import Player
from objects.beatmap import Beatmap

@dataclass
class Score:
    score_id: int
    pp: float
    mods: str
    score: int
    grade: str
    acc: float
    combo: int
    h300: int
    h100: int
    h50: int
    misscount: int
    player: Player
    map: Beatmap
    date: str
    leaderboard_rank: int = None