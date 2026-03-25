from odrx_py import APIClient

async def test():
    client = APIClient()
    user = await client.get_user(user_id=1, username="", from_username=False)
    
    return user