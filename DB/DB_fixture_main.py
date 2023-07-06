
# DB 서버 열기 
# DB 서버에서 league_id 를 불러오기
# league_id를 파라미터로 받는 함수를 통해 fixture를 불러서, 필요한 컬럼 (api_fixture_id , date, home_id, away_id)이중 리스트불러오기
# 그 리스트를 dictionary 형태로 변환
# 그 dict를 db로 박아넣기

import requests
from ETLServer.Modules.api_func import ApiFixtureBlock
from ETLServer.Modules.db_func import DBfunc

api_keys = "a68636f8f2c18511179c56f15e95080c"

DB_func = DBfunc()

api_func = ApiFixtureBlock()

DB_func.connectSQLServer()

league_id = DB_func.readTmpID()

data_list = api_func.load_fixtureData(league_id, api_keys)

dic_data = api_func.transform_fixtureData(data_list)

DB_func.insert_fixtureData(dic_data)

DB_func.closeSQLServer()



'''


DB_func.insertPipeTeamData(dicList)

DB_func.closeSQLServer()


'''