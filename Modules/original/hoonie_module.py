from ETLServer.Modules.load_toLocalJson import * 
from ETLServer.Modules import convertJson as js
from ETLServer.Modules import yoda_loadJson_block as load
from ETLServer.Modules import httpRes_func as hf
import requests, time

def load_API():
    league_id = 39
    season = 2022
    uri = f"https://v3.football.api-sports.io/teams?league={league_id}&season={season}"
    headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': 'e6b9fb7ce7a7ad7b239595f76e546384'
    }
    start_time = time.time()
    response = requests.request("GET", uri, headers = headers)
    response_time = hf.resTime(start_time)
    status = response.headers

    url = hf.getUrl(uri)[0]
    arguments = hf.getUrl(uri)[1]
    finalList = hf.getTimeStamp(status)
    finalCrudOpt = hf.getCrudOpt(status)
    finalstatus = hf.httpStatus(response)
    finalDict = js.convertToJson(response_time, finalCrudOpt, url, finalList[0], finalList[1], finalstatus)
