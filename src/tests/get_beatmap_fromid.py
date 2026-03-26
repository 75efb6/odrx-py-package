from odrx_py import APIClient


async def test():
    client = APIClient()
    bmap = await client.get_beatmap_fromid(map_id=1488203)

    return print(bmap)
