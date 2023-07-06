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

# # fixtures_main
# apiFunc = ApiFixtures(now_date,now_date_local)
# tmp_fixtureId = db_func.read_fixtureId(now_date)
# apiFunc.load_fixtureJson(now_date, tmp_fixtureId, api_keys)

# # fixtures_lineups
# api_func = ApiFixtureLineups(now_date, now_date_local)
# fixture_id = db_func.read_fixtureId(now_date)
# api_func.load_lineUpsJson(fixture_id, api_keys)

# # events
# api_func = ApiEvents(now_date, now_date_local)
# fixture_id = db_func.read_fixtureId(now_date)
# api_func.load_eventsJson(fixture_id, api_keys)

# # fixtures_Pstats
# api_func = ApiFixturePStats(now_date,now_date_local)
# fixture_id = db_func.read_fixtureId(now_date)
# api_func.load_fixturePStatsJson(fixture_id,api_keys)

# # fixtures_Tstats
# api_func = ApiFixtureTStats(now_date,now_date_local)
# fixture_id = db_func.read_fixtureId(now_date)
# api_func.load_fixtureTStatsJson(fixture_id, api_keys)

# # fixtures_H2h
# api_func = ApiH2h(now_date,now_date_local)
# round_data = db_func.read_roundInfo(now_date)
# api_func.load_h2hJson(round_data, api_keys)

# # leagues
# api_func = ApiLeagues(now_date, now_date_local)
# tmp_leagueId = db_func.read_leagueId()
# api_func.load_leagueJson(tmp_leagueId, api_keys)

# # players/players
# api_func = ApiPlayerPlayers(now_date, now_week,now_date_local)
# teamId = db_func.read_tlId()
# api_func.load_pplayerJson(teamId, api_keys)

# # predictions
# api_func = ApiPredictions(now_date, now_date_local)
# fixture_id = db_func.read_fixtureId(now_date)
# api_func.load_predictionsJson(fixture_id, api_keys)

# # players/squads
# api_func = ApiPsquad(now_date, now_date_local)
# teamId = db_func.read_teamId()
# api_func.load_psquadJson(teamId, api_keys)

# # players/Tscorers
# api_func = ApiPtopscoreres(now_date, now_date_local)
# tmp_leagueId = db_func.read_leagueId()
# api_func.load_ptopscorersJson(tmp_leagueId, api_keys)

# # standings
# api_func = ApiStandings(now_date, now_date_local)
# tmp_leagueId = db_func.read_tmpLeagueId()
# api_func.load_standingJson(tmp_leagueId, api_keys)

# NEED TO FIX !!!!!!!!!!!!!!!!!!
# # teams
# api_func = ApiTeams(now_date, now_date_local)
# tmp_leagueId = db_func.read_tmpLeagueId()
# api_func.load_teamJson(tmp_leagueId, api_keys)

# # teams/statistics
# api_func = ApiTeamStatistics(now_date, now_date_local)
# tmp_TeamLeagueId = db_func.read_LeagueTeamId()
# api_func.Api_TstatsJson(tmp_TeamLeagueId, api_keys, round_date=now_date)