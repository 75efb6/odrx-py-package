from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    scores = await client.get_recent_score(user_id=1)

    return print(scores)
