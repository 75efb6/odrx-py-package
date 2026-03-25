import utils.parser
import utils.helpers

from handlers.request import AsyncRequestHandler

from objects.player import Player
from objects.score import Score

class APIClient:
    def __init__(self):
        self.api = AsyncRequestHandler()
        self.endpoints = {
            "get_user": "/get_user"
        }

    
    async def get_user(self, user_id: int = None, username: str = None, from_username: bool = False) -> Player:
        utils.helpers.check_get_user_attrs(uid=user_id, username=username, from_username=from_username)
        
        req = await self.api.get(self.endpoints["get_user"]+f"?id={user_id}") if from_username is False else await self.api.get(self.endpoints["get_user"]+f"?username={username}")

        return utils.parser.player(req)