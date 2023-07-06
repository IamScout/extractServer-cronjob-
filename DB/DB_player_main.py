import requests
from ETLServer.Modules.api_func import ApiPlayerBlock
from ETLServer.Modules.db_func import DBfunc


api_keys = "a68636f8f2c18511179c56f15e95080c"

#db func 불러오기 위해서 class 생성
DB_func = DBfunc()

#api_func 불러오기 위해서 class 생성
api_func = ApiPlayerBlock()

#기능 실행 [sql server 붙이기]
DB_func.connectSQLServer()

#기능 실행 [sql server에서 적재되어있는 api_league_id 리스트 적재]
tempId = DB_func.readTeamId()

print(tempId)
print(len(tempId))

tempApi = api_func.loadPlayerData(tempId, api_keys)

print(tempApi)

dicList = api_func.transformPlayerData(tempApi)

DB_func.insertPlayerData(dicList)

DB_func.closeSQLServer()