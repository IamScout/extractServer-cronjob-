'''
[Need to Know]
- 이건 수정 안했음....ㅎ.ㅎ
'''

#DB로 가는 api_func 스크립트 


import requests, time
from ETLServer.Modules import http_response as hf
from ETLServer.Modules import convert_toJson as js
from ETLServer.Modules import load_json as load


class API_block:

    def load_pipe_league_API(self, idList, api_keys):
        print("load league ID start")

        dataList = []

        for i in idList:
            leagueID = i
            print(leagueID)
            season = 2022
            uri = "https://v3.football.api-sports.io/leagues?id=%s&season=%d" % (leagueID, season)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            startTime = time.time()
            resp = requests.request("GET", uri, headers=headers)
            data = resp.json()['response']

            status = resp.headers

            finalTime = hf.resTime(startTime)
            finalUrl = hf.getUrl(uri)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            print(finalstatus)
            finalDict = js.convert_toJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

            data_1 = data[0]
            dataList.append(data_1)
            print(dataList)

        return dataList

    def tmp_pipe_league_API(self, dataList):
        dictList = []

        for i in dataList:
            league_name = i['league']['name']
            api_league_id = i['league']['id']
            league_nation = i['country']['name']
            dataDict = {"league_name": league_name, "api_league_id": api_league_id, "league_nation": league_nation}
            dictList.append(dataDict)

        return dictList


class ApiTeamBlock:

    def loadTeamData(self, idList, api_keys):
        print("load Team ID start")

        dataList = []

        for i in idList:
            leagueId = i
            season = 2022

            uri = "https://v3.football.api-sports.io/teams?league=%s&season=%d" % (leagueId, season)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            startTime = time.time()
            resp = requests.request("GET", uri, headers=headers)
            data = resp.json()['response']

            for j in range(len(data)):
                tmpList = []
                tmpData = data[j]
                tmpList.append(i)
                tmpList.append(tmpData)
                dataList.append(tmpList)

            print("load compelete league ID : %s" % leagueId)

            status = resp.headers

            finalTime = hf.get_responseTime(startTime)
            finalUrl = hf.get_uriInfos(uri)
            finalTimeStamp = hf.get_timeStamp(status)
            finalCrudOpt = hf.get_crudOption(status)
            finalstatus = hf.get_httpStatus(resp)
            # print(finalstatus)
            finalDict = js.convert_toJson(finalTime, finalCrudOpt, finalUrl, finalTimeStamp, finalstatus)

            load.load_json(finalDict)

        # print(dataList)

        return dataList

    def transformTeamData(self, dataList):
        dictList = []

        for i in dataList:
            teamName = i[1]['team']['name']
            apiTeamId = i[1]['team']['id']
            apiLeagueID = i[0]
            print(apiLeagueID)
            dataDict = {"teamName": teamName, "apiTeamId": apiTeamId,"apiLeagueId": apiLeagueID}
            dictList.append(dataDict)

        return dictList


class ApiPlayerBlock:

    def loadPlayerData(self, idList, api_keys):
        print("load Player ID start")

        dataList = []

        for i in range(1, len(idList) + 1):

            if i % 200 == 0:
                time.sleep(60)
            else:
                pass

            teamId = idList[i-1]

            uri = "https://v3.football.api-sports.io/players/squads?team=%d" % teamId

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            startTime = time.time()
            resp = requests.request("GET", uri, headers=headers)
            data = resp.json()['response']

            for j in range(len(data)):
                tmpData = data[j]
                dataList.append(tmpData)

            print("load compelete team ID : %s" % teamId)

            status = resp.headers

            finalTime = hf.resTime(startTime)
            finalUrl = hf.getUrl(uri)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            # print(finalstatus)
            finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

        # print(dataList)

        return dataList

    def transformPlayerData(self, dataList):
        dictList = []

        for i in dataList:
            tmpShell = i['players']
            for j in range(len(tmpShell)):
                print(tmpShell[j])
                playerName = tmpShell[j]['name']
                apiPlayerId = tmpShell[j]['id']
                dataDict = {"playerName": playerName, "apiPlayerId": apiPlayerId}
                dictList.append(dataDict)
        return dictList


class ApiFixtureBlock:
    
    def load_fixtureData(self, idList, api_keys):

        season = 2022
        timezone = "europe/london"
        dataList =[]

        print("load fixture data start")

        for i in idList:
            league_id = i

            base_url = "https://v3.football.api-sports.io/fixtures?league=%d&season=%d&timezone=%s" %(league_id, season, timezone)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            start_time = time.time()
            resp = requests.request("GET", base_url, headers= headers)
            data = resp.json()['response']
            
            for j in range(len(data)):
                tmpData = data[j]
                dataList.append(tmpData)
                

            print("params : %d load list complete!" %league_id)

            status = resp.headers

            finalTime = hf.resTime(start_time)
            finalUrl = hf.getUrl(base_url)
            finalList = hf.getTimeStamp(status)
            finalCrudOpt = hf.getCrudOpt(status)
            finalstatus = hf.httpStatus(resp)
            # print(finalstatus)
            finalDict = js.convertToJson(finalTime, finalCrudOpt, finalUrl, finalList[0], finalList[1], finalstatus)

            load.loadMonitoringJson(finalDict)

        return dataList

    def transform_fixtureData(self, data_list):
        dict_list = []

        for i in data_list:
            tmp_fixtureId = i['fixture']['id']
            tmp_fixtureDate = i['fixture']['date']
            tmp_fixtureHomeId = i['teams']['home']['id']
            tmp_fixtureAwayId = i['teams']['away']['id']
            data_dict = {"fixture_id" : tmp_fixtureId, "fixture_date" : tmp_fixtureDate, "fixture_home_id" : tmp_fixtureHomeId, "fixture_away_id": tmp_fixtureAwayId}
            dict_list.append(data_dict)

        return dict_list



class ApiUpdateFixture:

    def update_todayRoundFixture(self, data_list, api_keys):

        print("run func update_todayRoundFixutre")
        timezone = 'europe/london'
        update_data = []

        for fixture_id in data_list:
            
            tmp_dataList =[]

            base_url = "https://v3.football.api-sports.io/fixtures?id=%s&timezone=%s" %(fixture_id, timezone)

            headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
            }

            start_time = time.time()
            resp = requests.request("GET", base_url , headers = headers)
            data = resp.json()['response'][0]

            tmp_dataList.append(data['fixture']['id'])
            tmp_dataList.append(data['fixture']['date'])
            tmp_dataList.append(data['teams']['home']['id'])
            tmp_dataList.append(data['teams']['away']['id'])

            update_data.append(tmp_dataList)
            print("load comeplete %s" %data['fixture']['id'])

        return update_data

            



            






