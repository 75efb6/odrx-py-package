from ..utils import RequestHandler, parser
from ..classes import Beatmap, Player, Score
from ..enums import Endpoints


class ODRXAPIClient:
    def __init__(self, whitelist_key: str = None):
        self.api = RequestHandler()
        self.key = whitelist_key
        self.endpoints: Endpoints = Endpoints

    def get_user_fromid(self, user_id: int) -> Player:
        req = self.api.get(self.endpoints.GET_USER + f"?id={user_id}")

        return parser.player(req)

    def get_user_fromusername(self, username: str) -> Player:
        req = self.api.get(self.endpoints.GET_USER + f"?username={username}")

        return parser.player(req)

    def get_beatmap_fromid(self, map_id: int) -> Beatmap:
        req = self.api.get(self.endpoints.BEATMAP + f"?bid={map_id}")

        return parser.beatmap(req)

    def get_beatmap_frommd5(self, md5: str) -> Beatmap:
        req = self.api.get(self.endpoints.BEATMAP + f"?md5={md5}")

        return parser.beatmap(req)

    def get_beatmap_leaderboard_fromid(self, map_id: int) -> list[Score]:
        req = self.api.get(
            self.endpoints.BEATMAP_LEADERBOARD + f"?bid={map_id}"
        )

        return parser.beatmap_leaderboard(req)

    def get_beatmap_leaderboard_frommd5(self, md5: str) -> list[Score]:
        req = self.api.get(self.endpoints.BEATMAP_LEADERBOARD + f"?md5={md5}")

        return parser.beatmap_leaderboard(req)

    def get_leaderboard(
        self, type: str = "pp", country: str = None
    ) -> list[Player]:
        if type not in ["pp", "score"]:
            raise ValueError("Invalid leaderboard type. Must be 'pp' or 'score'.")

        req = self.api.get(
            self.endpoints.LEADERBOARD
            + f"?type={type}"
            + (f"&country={country}" if country else "")
        )

        return parser.leaderboard(req)

    def get_top_scores(self, user_id: int) -> list[Score]:
        req = self.api.get(
            self.endpoints.TOP_SCORES + f"?id={user_id}&limit=100"
        )

        return [parser.score(score) for score in req]

    def get_recent_score(self, user_id: int, offset: int = 0) -> list[Score]:
        req = self.api.get(
            self.endpoints.GET_RECENT + f"?id={user_id}&offset={offset}"
        )

        return parser.score(req)

    def get_scores_uid_beatmap_fromid(self, user_id: int, map_id: int) -> Beatmap:
        req = self.api.get(
            self.endpoints.BEATMAP_SCORE + f"?id={map_id}&uid={user_id}"
        )

        return parser.beatmap(req)

    def get_scores_uid_beatmap_frommd5(self, user_id: int, md5: str) -> Beatmap:
        req = self.api.get(
            self.endpoints.BEATMAP_SCORE + f"?md5={md5}&uid={user_id}"
        )

        return parser.beatmap(req)

    def get_scores_uname_beatmap_fromid(
        self, username: str, map_id: int
    ) -> Beatmap:
        req = self.api.get(
            self.endpoints.BEATMAP_SCORE + f"?id={map_id}&username={username}"
        )

        return parser.beatmap(req)

    def get_scores_uname_beatmap_frommd5(
        self, username: str, md5: str
    ) -> Beatmap:
        req = self.api.get(
            self.endpoints.BEATMAP_SCORE + f"?md5={md5}&username={username}"
        )

        return parser.beatmap(req)

    def get_whitelist(
        self,
    ) -> list[
        Beatmap
    ]:  # Shit takes a long time to succeed, if it even does at all LMAO.
        req = self.api.get(self.endpoints.WHITELIST)

        return [parser.beatmap(map) for map in req]

    def whitelist_add_fromid(self, map_id: int) -> Beatmap:
        if not self.key:
            raise ValueError("Whitelist key is required for this endpoint.")

        bmap = self.api.get(
            self.endpoints.WHITELIST_ADD + f"?id={map_id}&key={self.key}"
        )
        return parser.beatmap(bmap)

    def whitelist_add_frommd5(self, md5: str) -> str:
        if not self.key:
            raise ValueError("Whitelist key is required for this endpoint.")

        self.api.get(
            self.endpoints.WHITELIST_ADD + f"?md5={md5}&key={self.key}"
        )
        return "Beatmap added to whitelist."
