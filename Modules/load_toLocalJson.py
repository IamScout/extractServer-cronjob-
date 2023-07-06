'''
[Code Explanation]
- 리그의 standing 정보를 json 파일에 적재하는 모듈
- 런던의 utc 협정 시간대 적용
- 파일 저장 형태 :'[날짜]_[리그]id_standing.json'

[Need to Know]
- 24번째 줄의 try/except 구문은 테스트용 파일 생성자이므로 추후 삭제 필요
'''

import json
import os
from datetime import datetime

# standing - 매일
# [년월일]_standings.json

def load_standingJson(now_date, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) -1 )
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'standings', now_year) #

    with open("%s/%s_standing.json" % (directory, now_date), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_standing.json" % (directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# fixture/fixture - 1년
# 시즌(22)_[리그 ID]_fixture.json
# 변수로 리그ID 필요

def load_fixtureJson(now_date, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'fixtures', now_year) #

    with open("%s/%s_fixture.json" % (directory, now_date), "r") as json_file:
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    # print(tmp_data)

    with open("%s/%s_fixture.json" % (directory, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Load is done!")



#################################################33
# teams/statistics - 매일
# [리그 ID]_Tstats.json
# 변수로 리그ID 필요

def load_TstatsJsonData(now_date_local, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'teams', 'Statistics', now_year) #

    with open("%s/%s_Tstats.json" % (directory, now_date_local), "r") as json_file: #
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    with open("%s/%s_Tstats.json" % (directory, now_date_local), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# teams/information - 1년
# [리그 ID]_Tinfo.json
# 변수로 리그ID 필요

def load_TinfosJson(now_date, tmp_data, league_id): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'teams', 'Info', now_year) #

    with open("%s/%d_Tinfo.json" % (directory, league_id), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%d_Tinfo.json" % (directory, league_id), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# fixtures/head to head - 매일
# [년월일]_h2h.json

def load_h2hJson(now_date, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'H2h', now_year) #

    with open("%s/%s_h2h.json" %(directory, now_date), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_h2h.json" %(directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# fixtures/events - 매일
# [년월일]_events.json

def load_eventsJson(now_date, tmp_data):
    
    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) -1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'events', now_year) #

    with open("%s/%s_events.json" %(directory, now_date), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_events.json" %(directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")


################################################################
# fixtures/team statistics - 매일
# [리그 ID]_Ftstats.json

def load_fixtureTStatsJsonData(now_date, tmp_data):

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'Tstatistics', now_year) #

    with open("%s/%s_Tstatistics.json" % (directory, now_date), "r") as json_file: #
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    with open("%s/%s_Tstatistics.json" % (directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# fixtures/players statistics - 매일
# [년월일]_Pstatistics.json

def load_fixturePStatsJsonData(now_date, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'Pstatistics', now_year) #

    with open("%s/%s_Pstatistics.json" % (directory, now_date), "r") as json_file: #
        data = json.load(json_file)
     
    data['data'].append(tmp_data)

    with open("%s/%s_Pstatistics.json" % (directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# fixtures/lineups - 매일
# [년월일]_lineups.json

def load_lineUpsJson(now_date, tmp_data): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'fixtures', 'lineups', now_year) #

    with open("%s/%s_lineUps.json" %(directory, now_date), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_lineUps.json" %(directory, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# leagues - 1년
# [리그 ID]_leagueInfo.json

def load_leagueJson(now_date, tmp_data, league_id):

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'leagues', now_year) #

    with open("%s/%d_leagueInfo.json" % (directory, league_id), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%d_leagueInfo.json" % (directory, league_id), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# players/squads - 1년
# [팀 ID]_Psquad.json

def load_psquadJson(now_date, tmp_data, team_id): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'players', 'Squads', now_year) #

    with open("%s/%d_Psquad.json" % (directory, team_id), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%d_Psquad.json" % (directory, team_id), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# teams/coach

# def load_coachsJsonData(tmp_data, league_id):

#     now_date = datetime.utcnow().date().strftime("%y%m%d")
#     directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'coachs')

#     with open("%s/%s/%s_%d_coachs.json" % (directory, now_date, now_date, league_id), "r") as json_file:
#         data = json.load(json_file)

#     data['data'].append(tmp_data)
#     print(tmp_data)

#     with open("%s/%s/%s_%d_coachs.json" % (directory, now_date, now_date, league_id), "w") as json_file:
#         json.dump(data, json_file, indent=4)
#        print("Load is done!")



# players/players - 1주
# [리그 ID]_players.json
""" 대대적인 수정 필요"""
def load_pplayerJson(now_date, now_week, tmp_data, league_id): #

    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) -1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'players', 'Players', now_year, now_week) #

    with open("%s/%s_players.json" % (directory, league_id), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_players.json" % (directory, league_id), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# players/top scorers - 매일
# [리그 ID]_Ptopscorers.json

def load_ptopscorersJson(now_date, tmp_data):

    now_year = datetime.utcnow().date().strftime("%Y")
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'players', 'Topscorers', now_year) #

    with open("%s/%s_Ptopscorers.json" % (directory, now_date), "r") as json_file: #
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_Ptopscorers.json" % (directory, now_date), "w") as json_file: #
        json.dump(data, json_file, indent=4)
        print("Load is done!")



# predictions - 매일
# [년월일]

def load_predictionsJsonData(now_date, tmp_data):
    now_year = datetime.utcnow().date().strftime("%Y") #
    now_year = str(int(now_year) - 1)
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'predictions', now_year) #

    with open("%s/%s_predictions.json" % (directory, now_date), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_data)

    with open("%s/%s_predictions.json" % (directory, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("Load is done!")