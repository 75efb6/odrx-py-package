from odrx_py import APIClient


async def test():
    client = APIClient()
    user = await client.get_user_fromid(user_id=1)

    return print(user)
