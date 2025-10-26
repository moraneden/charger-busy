# program that check api https://github.com/moraneden/charger-busy and return the status of the charger
# use fastapi to create the api

from fastapi import FastAPI
from fastapi.responses import FileResponse
from charger import ChargerChecker
import uvicorn
from itertools import chain

app = FastAPI()
charger_checker = ChargerChecker()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/status")
def read_status():
    res = []
    res.append(charger_checker.get_status("https://cp.evedge.co.il/api/v2/app/locations", 322))
    res.append(charger_checker.get_status("https://cp.evedge.co.il/api/v2/app/locations", 768))
    res.append(charger_checker.get_status("https://cp.scala-ev.com/api/v2/app/locations", 259))
 
    merged = {
        "locations": list(chain.from_iterable(obj.get("locations", []) for obj in res)),
        "tariffs": [],
        "currencies": []
    }
    print(merged) 
    return merged


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")


                