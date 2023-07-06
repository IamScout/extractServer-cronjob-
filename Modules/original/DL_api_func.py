import requests, time
from ETLServer.Modules.load_toLocalJson import * 
from ETLServer.Modules import convertJson as js
from ETLServer.Modules import yoda_loadJson_block as load
from ETLServer.Modules import httpRes_func as hf

class ApiStandings:

	def load_standingJson(self, idList, api_keys):
		print("run func load_standingJson")

		for i in idList:

			season = 2022
			leagueId = i
			print("call api req -> params : %d" %leagueId)

			base_Url = "https://v3.football.api-sports.io/standings?league=%d&season=%d" %(leagueId, season)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }
			
			start_time = time.time()
			resp = requests.request("GET",base_Url, headers=headers)
			data_raw = resp.json()['response']

			status = resp.headers

            finalTime = hf.resTime(startTime)
            finalUrl = hf.getUrl(uri)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            print(finalstatus)
            finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

			load_standingJson(data_raw, leagueId)

class ApiFixtures:

	#def load_fixtureJson(self, idList, api_keys):

			


