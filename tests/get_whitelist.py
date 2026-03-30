from odrx_py import APIClient


async def test():
    client = APIClient()
    wl = await client.get_whitelist()

    return print(wl)
