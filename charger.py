import requests

class ChargerChecker:
    def __init__(self):
        pass

    def check(self):
        url = "https://cp.evedge.co.il/api/v2/app/locations"
        try:
            payload = {"locations":{"322":None}}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(str(e))
            return {"error": str(e)}
