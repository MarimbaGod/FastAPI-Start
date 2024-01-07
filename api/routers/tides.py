from fastapi import FastAPI
import requests
# Import Additional for email, scheduling, etc

app = FastAPI()

@router.get("/fetch-tide-data")
def fetch_tide_data():
    #
    #
    return {"data": "Processed Tide data"}



@router.get("/tide-data/san-diego")
async def san_diego_data():
    url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=latest&station=9410170&product=water_level&datum=STND&time_zone=lst&units=english&format=json"

    params = {
        "date": "latest",
        "station": "9410170",
        "product": "water_level",
        "datum": "STND",
        "time_zone": "lst",
        "units": "english",
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
