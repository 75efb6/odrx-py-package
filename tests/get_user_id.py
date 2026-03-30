from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    user = await client.get_user_fromid(user_id=1)

    return print(user)
