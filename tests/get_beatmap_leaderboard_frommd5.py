from odrx_py import APIClient


async def test():
    client = APIClient()
    bmap = await client.get_beatmap_leaderboard_frommd5(
        md5="e551fcecceb8b784613602f19ff7348f"
    )

    return print(bmap)
