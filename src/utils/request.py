import aiohttp

class AsyncRequestHandler:
    def __init__(self):
        self.url = "https://v4rx.me/api"

    async def get(self, endpoint: str) -> dict:
        async with aiohttp.ClientSession() as session:
            full_url = self.url + endpoint
            try:
                async with session.get(full_url) as response:
                    if response.status == 200:
                        res = await response.json()
                        if (
                            endpoint == "/wl"
                        ):  # Goofy aah fix for the whitelist endpoint since it has a different response format
                            return res
                        return res.get("data")
                    else:
                        raise Exception("Status code is not 200.")
            except Exception as err:
                raise Exception(err)
