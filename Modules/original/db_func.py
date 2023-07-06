import mysql.connector

class DBfunc:

	def connectSQLServer(self):
		self.conn = mysql.connector.connect(user='root', password= 'tmzkdnxj1', host='34.64.214.96', database = 'scout', port = '3306')
		print("Hi! SQL")
		self.cursor = self.conn.cursor()

	def closeSQLServer(self):
		self.conn.close()
		print("BYE! SQL")


	def readTmpID(self):
		listID = []

		readQuery = 'select * from tmp_league'
		self.cursor.execute(readQuery)
		tmpListRaw = self.cursor.fetchall()
		for i in range(len(tmpListRaw)):
			listID.append(tmpListRaw[i][0])

		return listID

	def insertPipeLeagueData(self,data):

		for i in range(len(data)):
			insertDataList = []
			insertDataList.append(data[i]['league_name'])
			insertDataList.append(data[i]['api_league_id'])
			insertDataList.append(data[i]['league_nation'])
			insertSql = 'insert into pipe_league (league_name, api_league_id,league_nation) values ("%s",%d,"%s")' %(insertDataList[0],insertDataList[1],insertDataList[2])
			self.cursor.execute(insertSql)
			# print("insert Done!")
			self.conn.commit()


	def readLeagueId(self):
		listId = []

		readQuery = 'select api_league_id from pipe_league'
		self.cursor.execute(readQuery)
		tmpListRaw = self.cursor.fetchall()
		for i in range(len(tmpListRaw)):
			listId.append(tmpListRaw[i][0])

		return listId


	def insertPipeTeamData(self,data):
		for i in range(len(data)):
			tmpInsertDataList =[]
			tmpInsertDataList.append(data[i]['teamName'])
			tmpInsertDataList.append(data[i]['apiTeamId'])
			insertQuery = 'insert into pipe_team (team_name, api_team_id) values ("%s", %d)' %(tmpInsertDataList[0], tmpInsertDataList[1])
			self.cursor.execute(insertQuery)
			print("insert %s compelete" %tmpInsertDataList[0])
			self.conn.commit()

	def readTeamId(self):
		listId = []

		readQuery = 'select api_team_id from pipe_team'
		self.cursor.execute(readQuery)
		tmpListRaw = self.cursor.fetchall()
		for i in range(len(tmpListRaw)):
			listId.append(tmpListRaw[i][0])

		return listId

	def insertPlayerData(self,data):
		for i in range(len(data)):
			tmpInsertDataList =[]
			tmpInsertDataList.append(data[i]['playerName'])
			tmpInsertDataList.append(data[i]['apiPlayerId'])
			insertQuery = 'insert into pipe_player (player_name, api_player_id) values ("%s", %d)' %(tmpInsertDataList[0], tmpInsertDataList[1])
			self.cursor.execute(insertQuery)
			print("insert %s compelete" %tmpInsertDataList[0])
			self.conn.commit()

	def insert_fixtureData(self,data):
		for i in range(len(data)):
			tmp_insertDataList = []
			tmp_insertDataList.append(data[i]['fixture_id'])
			tmp_insertDataList.append(data[i]['fixture_date'])
			tmp_insertDataList.append(data[i]['fixture_home_id'])
			tmp_insertDataList.append(data[i]['fixture_away_id'])
			insert_query = 'insert into pipe_round (api_fixture_id, date, home_team_id, away_team_id) values (%d, "%s", %d, %d)' %(tmp_insertDataList[0], tmp_insertDataList[1], tmp_insertDataList[2], tmp_insertDataList[3])
			self.cursor.execute(insert_query)
			print("insert %s complete" %tmp_insertDataList[0])
			self.conn.commit()