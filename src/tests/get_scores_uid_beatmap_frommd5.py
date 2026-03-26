from odrx_py import APIClient

async def test():
    client = APIClient()
    bmap = await client.get_scores_uid_beatmap_frommd5(user_id=1, md5="e551fcecceb8b784613602f19ff7348f")

    return print(bmap)