from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    wl = await client.get_whitelist()

    return print(wl)
