import utils.parser
import utils.helpers

from handlers.request import AsyncRequestHandler

from objects.player import Player
from objects.score import Score

class DroidAPIClient:
    def __init__(self):
        self.api = AsyncRequestHandler()
        self.endpoints = {
            "get_user": "/get_user"
        }

    
