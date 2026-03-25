from dataclasses import dataclass

@dataclass
class Stats:
    global_rank: int
    score_global_rank: int
    country_rank: int
    score_country_rank: int
    pp: float
    acc: float
    total_score: int
    ranked_score: int
    total_playcount: int