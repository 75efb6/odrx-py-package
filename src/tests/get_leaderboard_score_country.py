from odrx_py import APIClient

async def test():
    client = APIClient()
    lb = await client.get_leaderboard(type=1, country="US")

    return print(lb)