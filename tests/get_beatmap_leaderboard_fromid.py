from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    bmap = await client.get_beatmap_leaderboard_fromid(map_id=1488203)

    return print(bmap)
