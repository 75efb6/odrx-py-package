import httpx

class AsyncRequestHandler:
    def __init__(self):
        self.url = "https://v4rx.me/api"

    async def get(self, endpoint: str) -> dict:
        async with httpx.AsyncClient(follow_redirects=True) as session:
            full_url = self.url + endpoint
            response = await session.get(full_url)
            response.raise_for_status()

            res = response.json()

            if (endpoint == "/wl"):  # Goofy aah fix for the whitelist endpoint since it has a different response format
                    return res
            
            return res.get("data")

class RequestHandler:
    def __init__(self):
        self.url = "https://v4rx.me/api"

    def get(self, endpoint: str) -> dict:
        full_url = self.url + endpoint

        with httpx.Client(follow_redirects=True) as session:
            res = session.get(full_url)
            res.raise_for_status()
            
            res_json = res.json()
            if (endpoint == "/wl"):  # Goofy aah fix for the whitelist endpoint since it has a different response format
                return res_json
            
            return res_json.get("data")
