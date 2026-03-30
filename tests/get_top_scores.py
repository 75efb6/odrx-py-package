from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    scores = await client.get_top_scores(user_id=1)

    return print(scores)
