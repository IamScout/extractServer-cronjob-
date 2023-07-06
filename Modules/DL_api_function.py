# load_fixtureJson이 now_date를 전달받도록 수정

import requests, time
import sys
sys.path.append("/etl")
import ETLServer_Re.Modules.load_toLocalJson as loadL
from ETLServer_Re.Modules.load_toLocalJson import *
import ETLServer_Re.Modules.convert_toJson as conv


class ApiStandings:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local

	def load_standingJson(self, idList, api_keys):
		print("run func load_standingJson")

		for i in idList:

			season = 2022
			league_id = i
			print("call api req -> params : %d" %league_id)

			uri = "https://v3.football.api-sports.io/standings?league=%d&season=%d" %(league_id, season)
			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}
			
			response = requests.request("GET",uri, headers=headers)
			
			try :
				data = response.json()['response'][0]
				print(f"Confirmed Standing data with parameter {league_id}")
			except : 
				data = {
				"league_id" : f"{league_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Standing data with parameter {league_id} ")

			loadL.load_standingJson(self.now_date_local, data)


# fixture id 받아와야 함!
class ApiFixtures:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_fixtureJson(self, now_date, idList, api_keys):

		print("run func load_fixtureJson")
		season = 2022
		timezone = 'Europe/London'
		
		for i in idList:
			fixture_id = i
			print("call api req -> params : %d" %fixture_id)

			uri = "https://v3.football.api-sports.io/fixtures?id=%d&season=%d&date=%s&timezone=%s" %(fixture_id, season, self.now_date, timezone)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers = headers)

			try :
				data = response.json()['response'][0]
				print(f"Confirmed Fixture data with parameter {fixture_id}")
			except :
				data = {
				"fixture" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture data with parameter {fixture_id}")

			loadL.load_fixtureJson(self.now_date_local, data)


class ApiTeamStatistics:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def Api_TstatsJson(self, idList, api_keys, round_date):
		print("run func load_TeamStatisticsJson")
		# print(round_date)

		cnt = 1
		for i in range(len(idList)):
			
			if cnt % 250 == 0:
				print('wait for 60s')
				time.sleep(60)
			else:
				pass

			season = 2022
			leagueId = idList[i][0]
			teamId = idList[i][1]
			print("call api req -> params_league : %d, params_team : %d" %(leagueId, teamId))

			uri = "https://v3.football.api-sports.io/teams/statistics?league=%d&season=%d&team=%d&date=%s" %(leagueId, season, teamId, round_date)
			headers = {
						'x-rapidapi-host': "v3.football.api-sports.io",
						'x-rapidapi-key': api_keys
						}

			response = requests.request("GET", uri, headers = headers)

			if response.json()['response'] == []:
				data = {
				"league, team" : f"{i}",
				"data" : "Not Supported"
			}
				print(f"Wrong Teams/Statistics data with parameter {i}")
			else:
				data = response.json()['response']
				print(f"Confirmed Teams/Statistics data with parameter {i}")
				
			final_dict = conv.convert_TstatsJson(data,round_date)
			loadL.load_TstatsJsonData(self.now_date_local, final_dict)
			cnt += 1


class ApiTeams:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	# league_id 리스트로 받아오기기
	def load_teamJson(self, idList, api_keys):

		print("run func load_fixtureJson")
		season = 2022
	
		for i in idList:
			league_id = i
			print("call api req -> params : %d" %league_id)

			uri = "https://v3.football.api-sports.io/teams?league=%dz&season=%d" %(league_id, season)

			headers = {
                'x-rapidapi-host': "v3.football.api-sports.io",
                'x-rapidapi-key': api_keys
			}
			response = requests.request("GET", uri, headers = headers)

			if response.json()['response'] == []:
				data = {
				"league_id" : f"{league_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Teams data with parameter {league_id}")
			else:
				data = response.json()['response']
				print(f"Confirmed Teams data with parameter {league_id}")

			loadL.load_TinfosJson(self.now_date_local, data, league_id)


class ApiH2h:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	
	def load_h2hJson(self,data_list, api_keys):
		print("run func load_h2hJson")

		for i in range(len(data_list)):
			home = data_list[i]['home_id']
			away =data_list[i]['away_id']
			date_day = data_list[i]['date']
			print(date_day)

			params = "%d-%d" %(home, away) 
			print("call api req -> params : %s" %params)

			uri = "https://v3.football.api-sports.io/fixtures/headtohead?h2h=%s&date=%s&timezone=%s" %(params, date_day, 'europe/london')
			
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys

			}

			response = requests.request("GET", uri, headers = headers)
			try :
				data = response.json()['response'][0]
				print(f"Confirmed Fixture/H2h data with parameter {params}")
			except : 
				data = {
				"params" : f"{params}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/H2h data with parameter {params} ")

			loadL.load_h2hJson(self.now_date_local, data)


class ApiEvents:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_eventsJson(self,data_list, api_keys):
		print("run func eventsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print("call api req -> params : %s" %fixture_id)

			uri = 'https://v3.football.api-sports.io/fixtures/events?fixture=%d' %fixture_id

			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers= headers)

			if response.json()['response'] == []:
				data = {
				"fixture" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/Events data with parameter {fixture_id}")
				loadL.load_eventsJson(self.now_date_local, data)
			else:
				data = response.json()['response']
				print(f"Confirmed Fixture/Events data with parameter {fixture_id}")
				final_dict = conv.convert_eventsJson(data,fixture_id)
				loadL.load_eventsJson(self.now_date_local, final_dict)


class ApiFixtureTStats:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_fixtureTStatsJson(self, data_list, api_keys):
		print("run func load_fixtureTStatsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			# print(fixture_id)

			uri = "https://v3.football.api-sports.io/fixtures/statistics?fixture=%d" %fixture_id
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers = headers)
			
			if response.json()['response'] == []:
				data = {
				"fixture" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/Tstats data with parameter {fixture_id}")
				loadL.load_fixtureTStatsJsonData(self.now_date_local, data)
			else:
				data = response.json()['response']
				print(f"Confirmed Fixture/Tstats data with parameter {fixture_id}")
				final_dict = conv.convert_HomeAwayJson(data, fixture_id)
				loadL.load_fixtureTStatsJsonData(self.now_date_local, final_dict)


class ApiFixturePStats:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_fixturePStatsJson(self, data_list, api_keys):
		print("run func load_fixturePStatsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			# print(fixture_id)

			uri = "https://v3.football.api-sports.io/fixtures/players?fixture=%d" %fixture_id
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}


			response = requests.request("GET", uri, headers = headers)
			if response.json()['response'] == []:
				data = {
				"fixture" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/Pstats data with parameter {fixture_id}")
				loadL.load_fixturePStatsJsonData(self.now_date_local, data)
			else:
				data = response.json()['response']
				print(f"Confirmed Fixture/Pstats data with parameter {fixture_id}")
				final_dict = conv.convert_HomeAwayJson(data, fixture_id)
				loadL.load_fixturePStatsJsonData(self.now_date_local, final_dict)


class ApiFixtureLineups:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_lineUpsJson(self, data_list, api_keys):
		print("run func lineupsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print("call api req -> params : %s" %fixture_id)

			uri = 'https://v3.football.api-sports.io/fixtures/lineups?fixture=%d' %fixture_id

			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers= headers)
			if response.json()['response'] == []:
				data = {
				"fixture" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/Lineups data with parameter {fixture_id}")
				loadL.load_lineUpsJson(self.now_date_local, data)
			else:
				data = response.json()['response']
				print(f"Confirmed Fixture/Lineups data with parameter {fixture_id}")
				final_dict = conv.convert_HomeAwayJson(data, fixture_id)
				loadL.load_lineUpsJson(self.now_date_local, final_dict)


class ApiLeagues:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	# league_id 리스트로 받아오기기
	def load_leagueJson(self, data_list, api_keys):

		print("run func load_fixtureJson")
		season = 2022
		
		print("call api req -> params : %d" %season)
		for i in data_list:
			league_id = i
			uri = "https://v3.football.api-sports.io/leagues?season=%d&id=%d" %(season, league_id)

			headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers = headers)
			try :
				data = response.json()['response'][0]
				print(f"Confirmed League data with parameter {league_id}")
			except : 
				data = {
				"league_id" : f"{league_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong League data with parameter {league_id} ")

			loadL.load_leagueJson(self.now_date_local, data, i)


class ApiPsquad:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_psquadJson(self, data_list, api_keys):
			print("run func load_fixtureJson")
			season = 2022
			
			# print("call api req -> params : %d" %team_id)
			for i in data_list:
				team_id = i
				uri = "https://v3.football.api-sports.io/players/squads?team=%d" %(team_id)

				headers = {
					'x-rapidapi-host': "v3.football.api-sports.io",
					'x-rapidapi-key': api_keys
				}

				response = requests.request("GET", uri, headers = headers)
				if response.json()['response'] == []:
					data = {
					"team_id" : f"{team_id}",
					"data" : "Not Supported"
				}
					print(f"Wrong Players/Squads data with parameter {team_id}")
				else:
					data = response.json()['response']
					print(f"Confirmed Players/Squads data with parameter {team_id}")

				loadL.load_psquadJson(self.now_date_local, data, i) 


class ApiPlayerPlayers:
	def __init__(self, now_date, now_week, now_date_local):
		self.now_date = now_date
		self.now_week = now_week
		self.now_date_local = now_date_local	
	def load_pplayerJson(self, data_list, api_keys):
		print("run func load_pplayerJson")
		season = 2022

		for i in range(len(data_list)):
			print(data_list)
			print(data_list[i])
			tmp_leagueRaw = data_list[i].keys()
			tmp_leagueId =', '.join(tmp_leagueRaw)

			tmp_teamList = data_list[i][f'{tmp_leagueId}']

			for team_id in tmp_teamList:

				base_uri = "https://v3.football.api-sports.io/players?league=%s&team=%s&season=%s" %(tmp_leagueId, team_id, season)
				
				headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
				}

				response = requests.request("GET", base_uri, headers = headers)
				end_page = response.json()['paging']['total']
				
				tmp_data = []

				for current in range(1, end_page+1):
					
					final_uri = "https://v3.football.api-sports.io/players?league=%s&team=%s&season=%s&page=%d" %(tmp_leagueId, team_id, season, current)
					# print(final_uri)

					response = requests.request("GET", final_uri , headers = headers)
					
					if response.json()['response'] == []:
						data = {
						"team_id" : f"{team_id}",
						"data" : "Not Supported"
					}
						print(f"Wrong Players data with parameter {team_id}")
					else:
						data = response.json()['response']
						print(f"Confirmed Players data with parameter {team_id}")

					tmp_data.append(data)

				
				team_playerData = conv.convert_playerJson(team_id, tmp_data)
				loadL.load_pplayerJson(self.now_date_local, self.now_week, team_playerData, tmp_leagueId)
				print("compelete %d teamId " %team_id)

			print("league %s is done" %tmp_leagueId)
			time.sleep(30)

		print(data_list)




class ApiPtopscoreres:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_ptopscorersJson(self, data_list, api_keys):
		print("run func load_fixtureJson")
		season = 2022
		# print("call api req -> params : %d" %team_id)
		for i in data_list:
			league_id = i
			uri = "https://v3.football.api-sports.io/players/topscorers?league=%d&season=%d" %(league_id, season)

			headers = {
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}
			response = requests.request("GET", uri, headers = headers)

			if response.json()['response'] == []:
				data = {
				"league_id" : f"{league_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Players/Tscorers data with parameter {league_id}")
				loadL.load_ptopscorersJson(self.now_date_local, data)
			else:
				data = response.json()['response']
				print(f"Confirmed Players/Tscorers data with parameter {league_id}")
				final_dict = conv.convert_ptopscorersJson(data, league_id)
				loadL.load_ptopscorersJson(self.now_date_local, final_dict)


class ApiPredictions:
	def __init__(self, now_date, now_date_local):
		self.now_date = now_date
		self.now_date_local = now_date_local
	def load_predictionsJson(self, data_list, api_keys):
		print("run func load_predictionsJson")

		for i in range(len(data_list)):
			fixture_id = data_list[i]
			print(fixture_id)

			uri = "https://v3.football.api-sports.io/predictions?fixture=%d" %fixture_id
			headers={
				'x-rapidapi-host': "v3.football.api-sports.io",
				'x-rapidapi-key': api_keys
			}

			response = requests.request("GET", uri, headers = headers)

			try :
				data = response.json()['response'][0]
				print(f"Confirmed Fixture/Predictions data with parameter {fixture_id}")
				loadL.load_predictionsJsonData(self.now_date_local, data)
				
			except : 
				data = {
				"league_id" : f"{fixture_id}",
				"data" : "Not Supported"
			}
				print(f"Wrong Fixture/Predictions data with parameter {fixture_id} ")
				final_dict = conv.convert_predictionsJson(data, fixture_id)
				loadL.load_predictionsJsonData(self.now_date_local, final_dict)