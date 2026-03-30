from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    lb = await client.get_leaderboard(type="score", country="US")

    return print(lb)
