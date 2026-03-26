from odrx_py import APIClient

async def test():
    client = APIClient()
    scores = await client.get_recent_score(user_id=1)

    return print(scores)