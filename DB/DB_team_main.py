import requests
from ETLServer.Modules.api_func import ApiTeamBlock
from ETLServer.Modules.db_function import DBfunc

api_keys = "a86d420d0d8840c8e722e16cf9742f7b"

#db func 불러오기 위해서 class 생성 
DB_func = DBfunc()

#api_func 불러오기 위해서 class 생성
api_func = ApiTeamBlock()

#기능 실행 [sql server 붙이기] 
DB_func.connect_SQL()

#기능 실행 [sql server에서 적재되어있는 api_league_id 리스트 적재]
tempId = DB_func.read_leagueId()

#기능 실행 [적재한 league_id 를 통해 team id 가 적재 되어있는 api call 하여 필요한 데이터 만들기]
tempAPI = api_func.loadTeamData(tempId, api_keys)

#print(tempAPI)

#teamAPI 내에 데이터중에 필요한 부분만 extract
dicList = api_func.transformTeamData(tempAPI)

#가공된 데이터를 db로 밀어넣기
DB_func.load_team(dicList)

DB_func.close_SQL()





