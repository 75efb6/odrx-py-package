from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    bmap = await client.get_beatmap_frommd5(md5="e551fcecceb8b784613602f19ff7348f")

    return print(bmap)
