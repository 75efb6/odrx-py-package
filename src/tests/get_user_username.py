from odrx_py import APIClient

async def test():
    client = APIClient()
    user = await client.get_user_fromusername(username="elfbars")

    return print(user)