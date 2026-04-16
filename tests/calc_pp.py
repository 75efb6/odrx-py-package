from odrx_py.performance import PPCalculator
from pathlib import Path

async def test():
    beatmap = Path(__file__).parent / "resources" / "beatmap.osu"
    mods = [
        {"acronym": "RX"}
    ]
    calculator = PPCalculator(beatmap=beatmap, mods=mods)

    return print(calculator.calculate_performance())
