import requests

class ChargerChecker:
    def __init__(self):
        pass

    def check(self, location=322):
        try:
            self.get_status("", location)
        except Exception as e:
            print(str(e))
            return {"error": str(e)}
    
    def get_status(self, url, location):
        if not url:
            return {"error": "URL is required"}
        if not location:
            return {"error": "Location is required"}
        try:
            payload = {"locations":{location:None}}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(str(e))
            return {"error": str(e)}
