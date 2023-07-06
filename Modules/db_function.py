'''
[Code Explanation]
- scout Database 접속 및 query문 전송, 데이터 반환

[Need to Know]
-
'''

import mysql.connector

class DBfunc:

	# connectSQLServer > connect_SQL
	def connect_SQL(self):
		self.conn = mysql.connector.connect(user='root', password= 'tmzkdnxj1', host='34.64.214.96', database = 'scout', port = '3306')
		print("Hi! SQL")
		self.cursor = self.conn.cursor()

	# closeSQLServer > close_SQL
	def close_SQL(self):
		self.conn.close()
		print("BYE! SQL")

	# readTmpID > read_tmpLeagueId
	def read_tmpLeagueId(self):

		id_list = []
		read_query = 'select * from tmp_league'
		self.cursor.execute(read_query)
		league_id = self.cursor.fetchall()
		for i in range(len(league_id)):
			id_list.append(league_id[i][0])
		return id_list


	# insertPipeLeagueData > load_leagueData
	def load_leagueData(self, data):
		for i in range(len(data)):
			load_data = []
			load_data.append(data[i]['league_name'])
			load_data.append(data[i]['api_league_id'])
			load_data.append(data[i]['league_nation'])
			insert_query = 'insert into pipe_league (league_name, api_league_id,league_nation) values ("%s",%d,"%s")' %(load_data[0],load_data[1],load_data[2])
			self.cursor.execute(insert_query)
			self.conn.commit()


	# readLeagueId > read_leagueId
	def read_leagueId(self):
		# listId > id_list
		id_list = []
		# pipe_league(league_name, api_league_id, league_nation)
		read_query = 'select api_league_id from pipe_league'
		self.cursor.execute(read_query)
		league_id = self.cursor.fetchall()
		for i in range(len(league_id)):
			id_list.append(league_id[i][0])

		return id_list

	# insertPipeTeamData > load_team
	def load_team(self,data):
		for i in range(len(data)):
			data_list =[]
			data_list.append(data[i]['teamName'])
			data_list.append(data[i]['apiTeamId'])
			data_list.append(data[i]['apiLeagueId'])
			# print(data[i]['apiLeagueId'])
			insert_query = 'insert into pipe_team (team_name, api_team_id, api_league_id) values ("%s", %d, %d)' %(data_list[0], data_list[1], data_list[2])
			self.cursor.execute(insert_query)
			# print("insert %s complete" %data_list[0])
			self.conn.commit()

	# readTeamId > read_teamId
	def read_teamId(self):
		id_list = []
		read_query = 'select api_team_id from pipe_team'
		self.cursor.execute(read_query)
		team_id = self.cursor.fetchall()
		for i in range(len(team_id)):
			id_list.append(team_id[i][0])
		return id_list

	# insertPlayerData > load_player
	def load_player(self,data):
		for i in range(len(data)):
			load_data = []
			load_data.append(data[i]['playerName'])
			load_data.append(data[i]['apiPlayerId'])
			insertQuery = 'insert into pipe_player (player_name, api_player_id) values ("%s", %d)' %(load_data[0], load_data[1])
			self.cursor.execute(insertQuery)
			# print("insert %s compelete" %load_data[0])
			self.conn.commit()

	# written by woorek: pipe_round tb에서 date 가져오기
	def read_roundDate(self,now_Date):
		# print(now_Date)
		read_query = 'select distinct date from pipe_round where date LIKE "%s"' %(now_Date+str("%"))
		# print(read_query)
		self.cursor.execute(read_query)
		tmp_roundDate = self.cursor.fetchall()
		# print(tmp_roundDate)
		round_date = tmp_roundDate[0][0]
		# print(round_date)

		return round_date


	def read_LeagueTeamId(self):
		id_list = []
		read_query = 'select api_league_id,api_team_id from pipe_team'
		self.cursor.execute(read_query)
		sql_data = self.cursor.fetchall()
		for i in range(len(sql_data)):
			TeamLeagueId_list = []
			TeamLeagueId_list.append(sql_data[i][0])
			TeamLeagueId_list.append(sql_data[i][1])
			id_list.append(TeamLeagueId_list)
		return id_list


	def read_roundInfo(self, now_date):
		return_data = []
		now_date = now_date.replace('_','-')

		query = "select * from pipe_round where date(date) = '%s'" %now_date
		# print(query)
		self.cursor.execute(query)
		tmp_data = self.cursor.fetchall()
		for i in range(len(tmp_data)):
			tmp_date = tmp_data[i][2][:tmp_data[i][2].index('T')]
			#print(tmp_date)
			tmp_home_id = tmp_data[i][3]
			tmp_away_id = tmp_data[i][4]
			tmp_dict = {'home_id': tmp_home_id, 'away_id': tmp_away_id, 'date': tmp_date}
			return_data.append(tmp_dict)

		return return_data


	def read_fixtureId(self, now_date):
		# print("run func read_fixtureId")
		returning_list = []

		query = "select api_fixture_id from pipe_round where date(date) ='%s'" %now_date
		self.cursor.execute(query)
		tmp_data = self.cursor.fetchall()

		for i in range(len(tmp_data)):
			returning_list.append(tmp_data[i][0])

		return returning_list

	def read_tlId(self):
		tmp_leagueId = self.read_leagueId()
		
		return_list =[]

		for i in tmp_leagueId:
			tmp_teamList = []
			tmp_league = i

			query = 'select api_team_id from pipe_team where api_league_id = %s' %tmp_league
			self.cursor.execute(query)
			tmp_data = self.cursor.fetchall()

			for j in tmp_data:
				tmp_teamList.append(j[0])

			tmp_dict ={'%s' %tmp_league : tmp_teamList}
			return_list.append(tmp_dict)

		return return_list

	def update_fixture(self, update_data):

		for i in update_data:
			query = 'update pipe_round set date = "%s" where api_fixture_id = %s' %(i[1], i[0])
			self.cursor.execute(query)
			self.conn.commit()
			# print("update %s compelete" %i[0])
			


		





