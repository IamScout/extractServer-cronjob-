from datetime import datetime, timedelta
import sys
sys.path.append("/etl")
from ETLServer_Re.Modules.db_function import *
from ETLServer_Re.Modules.DL_api_function import * 

now_date = datetime.utcnow().date().strftime("%Y-%m-%d")
now_week = str(datetime.utcnow().date().today().isocalendar()[1])
now_date_local = datetime.utcnow().date().strftime("%y%m%d")
api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"
db_func = DBfunc()
db_func.connect_SQL()

# leagues
api_func = ApiLeagues(now_date, now_date_local)
tmp_leagueId = db_func.read_leagueId()
api_func.load_leagueJson(tmp_leagueId, api_keys)
