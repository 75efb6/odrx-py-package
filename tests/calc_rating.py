from odrx_py.rating import SRCalculator
from pathlib import Path

async def test():
    beatmap = Path(__file__).parent / "resources" / "beatmap.osu"
    mods = [
        {"acronym": "RX"}
    ]
    calculator = SRCalculator(beatmap=beatmap, mods=mods)

    return print(calculator.calculate_rating())
