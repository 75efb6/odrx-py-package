from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    lb = await client.get_leaderboard()

    return print(lb)
