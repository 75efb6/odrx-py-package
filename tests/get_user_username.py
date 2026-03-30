from odrx_py import AsyncODRXAPIClient


async def test():
    client = AsyncODRXAPIClient()
    user = await client.get_user_fromusername(username="elfbars")

    return print(user)
