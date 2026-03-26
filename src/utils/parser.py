from objects.beatmap import Beatmap
from objects.player import Player
from objects.score import Score
from objects.stats import Stats
from utils.helpers import ModHelper


def player(player: dict) -> Player:
    stats = player.get("stats")

    stats = Stats(
        global_rank=stats.get("pp_rank"),
        country_rank=stats.get("country_pp_rank"),
        score_global_rank=stats.get("score_rank"),
        score_country_rank=stats.get("country_score_rank"),
        pp=stats.get("pp"),
        acc=stats.get("acc"),
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
        ar=bmap.get("ar"),
        cs=bmap.get("cs"),
        od=bmap.get("od"),
        hp=bmap.get("hp"),
        mode=bmap.get("mode"),
        stars=bmap.get("star"),
        status=bmap.get("status"),
        lenght=bmap.get("lenght"),
    )


def score(score: dict) -> Score:
    mod_parser = ModHelper(mods=score.get("mods"))
    score["mods"] = mod_parser.parse

    return Score(
        score_id=score.get("id"),
        pp=score.get("pp"),
        mods=score.get("mods"),
        score=score.get("score"),
        grade=score.get("grade"),
        acc=score.get("accuracy"),
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
