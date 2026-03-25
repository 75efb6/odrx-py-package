import utils.parser
import utils.helpers

from handlers.request import AsyncRequestHandler

from objects.player import Player
from objects.score import Score
from objects.beatmap import Beatmap

class APIClient:
    def __init__(self):
        self.api = AsyncRequestHandler()
        self.endpoints = {
            "get_user": "/get_user",
            "get_recent": "/recent",
            "top_scores": "/top_scores",
            "beatmap": "/beatmap",
            "beatmap_leaderboard": "/beatmap_leaderboard",
            "leaderboard": "/leaderboard"
        }

    class LeaderboardType:
        0 == "pp"
        1 == "score"
    
    async def get_user(self, user_id: int = None, username: str = None, from_username: bool = False) -> Player:
        utils.helpers.check_get_user_attrs(uid=user_id, username=username, from_username=from_username)
        
        req = await self.api.get(self.endpoints["get_user"]+f"?id={user_id}") if from_username is False else await self.api.get(self.endpoints["get_user"]+f"?username={username}")

        return utils.parser.player(req)
    
    """async def get_beatmap_fromid(self, map_id: int) -> Beatmap:
        req = await self.api.get(self.endpoints["beatmap"]+f"?id={map_id}")

        return utils.parser.beatmap(req)
    
    async def get_beatmap_frommd5(self, md5: str) -> Beatmap:
        req = await self.api.get(self.endpoints["beatmap"]+f"?md5={md5}")

        return utils.parser.beatmap(req)
    
    async def get_beatmap_leaderboard_fromid(self, map_id: int) -> list[Score]:
        req = await self.api.get(self.endpoints["beatmap_leaderboard"]+f"?id={map_id}")

        return utils.parser.beatmap_leaderboard(req)
    
    async def get_beatmap_leaderboard_frommd5(self, md5: str) -> list[Score]:
        req = await self.api.get(self.endpoints["beatmap_leaderboard"]+f"?md5={md5}")

        return utils.parser.beatmap_leaderboard(req)"""
    
    async def get_leaderboard(self, type: LeaderboardType = 0, country: str = "None") -> list[Player]:
        req = await self.api.get(self.endpoints["leaderboard"]+f"?type={type}"+(f"&country={country}"if country != "None" else ""))

        return utils.parser.leaderboard(req)