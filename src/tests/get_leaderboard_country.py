from odrx_py import APIClient

async def test():
    client = APIClient()
    lb = await client.get_leaderboard(country="US")

    return print(lb)