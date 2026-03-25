from dataclasses import dataclass

# Dependencies for Player class
from objects.stats import Stats

@dataclass
class Player:
    id: int
    name: str
    country: str
    is_online: bool
    stats: Stats