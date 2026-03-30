from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    bmap = await client.get_scores_uid_beatmap_fromid(user_id=1, map_id=1488203)

    return print(bmap)
