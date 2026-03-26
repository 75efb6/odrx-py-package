import utils.helpers
import utils.parser
from handlers.request import AsyncRequestHandler
from objects.beatmap import Beatmap
from objects.player import Player
from objects.score import Score


class APIClient:
    def __init__(self, whitelist_key: str = None):
        self.api = AsyncRequestHandler()
        self.key = whitelist_key
        self.endpoints = {
            "get_user": "/get_user",
            "get_recent": "/recent",
            "top_scores": "/top_scores",
            "beatmap_score": "/get_beatmap_score",
            "beatmap": "/beatmap",
            "beatmap_leaderboard": "/beatmap_leaderboard",
            "leaderboard": "/leaderboard",
            "whitelist": "/wl",
            "whitelist_add": "/wl_add",
            "whitelist_remove": "/wl_remove",
        }

    async def get_user_fromid(self, user_id: int) -> Player:
        utils.helpers.check_get_user_attrs(uid=user_id)
        req = await self.api.get(self.endpoints["get_user"] + f"?id={user_id}")

        return utils.parser.player(req)

    async def get_user_fromusername(self, username: str) -> Player:
        utils.helpers.check_get_user_attrs(username=username)
        req = await self.api.get(self.endpoints["get_user"] + f"?username={username}")

        return utils.parser.player(req)

    async def get_beatmap_fromid(self, map_id: int) -> Beatmap:
        req = await self.api.get(self.endpoints["beatmap"] + f"?bid={map_id}")

        return utils.parser.beatmap(req)

    async def get_beatmap_frommd5(self, md5: str) -> Beatmap:
        req = await self.api.get(self.endpoints["beatmap"] + f"?md5={md5}")

        return utils.parser.beatmap(req)

    async def get_beatmap_leaderboard_fromid(self, map_id: int) -> list[Score]:
        req = await self.api.get(
            self.endpoints["beatmap_leaderboard"] + f"?bid={map_id}"
        )

        return utils.parser.beatmap_leaderboard(req)

    async def get_beatmap_leaderboard_frommd5(self, md5: str) -> list[Score]:
        req = await self.api.get(self.endpoints["beatmap_leaderboard"] + f"?md5={md5}")

        return utils.parser.beatmap_leaderboard(req)

    async def get_leaderboard(
        self, type: str = "pp", country: str = None
    ) -> list[Player]:
        if type not in ["pp", "score"]:
            raise ValueError("Invalid leaderboard type. Must be 'pp' or 'score'.")

        req = await self.api.get(
            self.endpoints["leaderboard"]
            + f"?type={type}"
            + (f"&country={country}" if country else "")
        )

        return utils.parser.leaderboard(req)

    async def get_top_scores(self, user_id: int) -> list[Score]:
        req = await self.api.get(
            self.endpoints["top_scores"] + f"?id={user_id}&limit=100"
        )

        return [utils.parser.score(score) for score in req]

    async def get_recent_score(self, user_id: int, offset: int = 0) -> list[Score]:
        req = await self.api.get(
            self.endpoints["get_recent"] + f"?id={user_id}&offset={offset}"
        )

        return utils.parser.score(req)

    async def get_scores_uid_beatmap_fromid(self, user_id: int, map_id: int) -> Beatmap:
        utils.helpers.check_get_user_attrs(uid=user_id)
        req = await self.api.get(
            self.endpoints["beatmap_score"] + f"?id={map_id}&uid={user_id}"
        )

        return utils.parser.beatmap(req)

    async def get_scores_uid_beatmap_frommd5(self, user_id: int, md5: str) -> Beatmap:
        utils.helpers.check_get_user_attrs(uid=user_id)
        req = await self.api.get(
            self.endpoints["beatmap_score"] + f"?md5={md5}&uid={user_id}"
        )

        return utils.parser.beatmap(req)

    async def get_scores_uname_beatmap_fromid(
        self, username: str, map_id: int
    ) -> Beatmap:
        utils.helpers.check_get_user_attrs(username=username)
        req = await self.api.get(
            self.endpoints["beatmap_score"] + f"?id={map_id}&username={username}"
        )

        return utils.parser.beatmap(req)

    async def get_scores_uname_beatmap_frommd5(
        self, username: str, md5: str
    ) -> Beatmap:
        utils.helpers.check_get_user_attrs(username=username)
        req = await self.api.get(
            self.endpoints["beatmap_score"] + f"?md5={md5}&username={username}"
        )

        return utils.parser.beatmap(req)

    async def get_whitelist(
        self,
    ) -> list[
        Beatmap
    ]:  # Shit takes a long time to succeed, if it even does at all LMAO.
        req = await self.api.get(self.endpoints["whitelist"])

        return [utils.parser.beatmap(map) for map in req]

    async def whitelist_add_fromid(self, map_id: int) -> Beatmap:
        if not self.key:
            raise ValueError("Whitelist key is required for this endpoint.")

        bmap = await self.api.get(
            self.endpoints["whitelist_add"] + f"?id={map_id}&key={self.key}"
        )
        return utils.parser.beatmap(bmap)

    async def whitelist_add_frommd5(self, md5: str) -> str:
        if not self.key:
            raise ValueError("Whitelist key is required for this endpoint.")

        await self.api.get(
            self.endpoints["whitelist_add"] + f"?md5={md5}&key={self.key}"
        )
        return "Beatmap added to whitelist."
