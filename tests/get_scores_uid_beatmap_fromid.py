from odrx_py import APIClient


async def test():
    client = APIClient()
    bmap = await client.get_scores_uid_beatmap_fromid(user_id=1, map_id=1488203)

    return print(bmap)
