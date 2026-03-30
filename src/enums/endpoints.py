from enum import StrEnum

class Endpoints(StrEnum):
    GET_USER: str = "/get_user"
    GET_RECENT: str = "/recent"
    TOP_SCORES: str = "/top_scores"
    BEATMAP_SCORE: str = "/get_beatmap_score"
    BEATMAP: str = "/beatmap"
    BEATMAP_LEADERBOARD: str = "/beatmap_leaderboard"
    LEADERBOARD: str = "/leaderboard"
    WHITELIST: str = "/wl"
    WHITELIST_ADD: str = "/wl_add"
    WHITELIST_REMOVE: str = "/wl_remove"