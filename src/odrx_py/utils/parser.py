from ..classes import Beatmap, Player, Score, Stats
from ..utils import ModHelper
from ..enums import BeatmapStatus, BeatmapMode


def player(player: dict) -> Player:
    stats = player.get("stats")

    stats = Stats(
        global_rank=stats.get("pp_rank"),
        country_rank=stats.get("country_pp_rank"),
        score_global_rank=stats.get("score_rank"),
        score_country_rank=stats.get("country_score_rank"),
        pp=round(float(stats.get("pp", 0)), 2),
        acc=round(float(stats.get("acc", 0)), 2),
        total_score=stats.get("tscore"),
        ranked_score=stats.get("rscore"),
        total_playcount=stats.get("plays"),
    )

    player = Player(
        id=player.get("id"),
        name=player.get("username"),
        country=player.get("country"),
        is_online=player.get("online", False),
        stats=stats,
    )

    return player


def beatmap(bmap: dict) -> Beatmap:
    return Beatmap(
        id=bmap.get("id"),
        set_id=bmap.get("set_id"),
        hash=bmap.get("md5"),
        artist=bmap.get("artist"),
        title=bmap.get("title"),
        version=bmap.get("version"),
        creator=bmap.get("creator"),
        ar=round(float(bmap.get("ar", 0)), 1),
        cs=round(float(bmap.get("cs", 0)), 1),
        od=round(float(bmap.get("od", 0)), 1),
        hp=round(float(bmap.get("hp", 0)), 1),
        mode=BeatmapMode(bmap.get("mode")).__str__(),
        stars=round(float(bmap.get("star", 0)), 2),
        status=BeatmapStatus(bmap.get("status")).__str__(),
        lenght=bmap.get("lenght"),
    )


def score(score: dict) -> Score:
    mod_parser = ModHelper(mods=score.get("mods"))
    score["mods"] = mod_parser.parse

    return Score(
        score_id=score.get("id"),
        pp=round(float(score.get("pp", 0)), 2),
        mods=score.get("mods"),
        score=score.get("score"),
        grade=score.get("grade"),
        acc=round(float(score.get("accuracy", 0)), 2),
        combo=score.get("max_combo"),
        h300=score.get("h300"),
        h100=score.get("h100"),
        h50=score.get("h50"),
        misscount=score.get("hmiss"),
        player=player(score.get("player")),
        map=beatmap(score.get("bmap")),
        date=score.get("date"),
        leaderboard_rank=score.get("rank"),
    )


def leaderboard(players: list[dict]) -> list[Player]:
    lb = []

    for p in players:

        p = player(p)

        lb.append(p)

    return lb


def beatmap_leaderboard(scores: list[dict]) -> list[Score]:
    lb = []

    rank = 0

    for s in scores:
        rank += 1
        s["rank"] = rank
        s = score(s)

        lb.append(s)

    return lb
