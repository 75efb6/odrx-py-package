from odrx_py import APIClient


async def test():
    client = APIClient()
    scores = await client.get_top_scores(user_id=1)

    return print(scores)
