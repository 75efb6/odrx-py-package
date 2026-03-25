from odrx_py import APIClient

async def test():
    client = APIClient()
    user = await client.get_user(username="elfbars", from_username=True)

    return print(user)