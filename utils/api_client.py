import requests

class APIClient:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }

    def get(self, url):
        return requests.get(url, headers=self.headers)

    def post(self, url, payload):
        return requests.post(url, json=payload, headers=self.headers)