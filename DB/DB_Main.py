import requests
from ETLServer.Modules.api_func import API_block
from ETLServer.Modules.db_func import DBfunc

api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

DB_func = DBfunc()

api_func = API_block()

DB_func.connectSQLServer()

tempId = DB_func.readTmpID()

tempAPI = api_func.load_pipe_league_API(tempId, api_keys)

dicList = api_func.tmp_pipe_league_API(tempAPI)


#DB_Func.insertPipeLeagueData(dicList)

DB_func.closeSQLServer()

