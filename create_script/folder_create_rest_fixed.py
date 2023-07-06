# Firture 외 나머지 폴더 생성 스크립트

# 모듈 불러오기
import os, sys, json
from datetime import datetime, timedelta

sys.path.append("/etl/ETLServer_Re")
from Modules.db_function import *

# 공통 디렉토리
# directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')

# 도훈's 디렉토리
directory = "/etl/ETLServer_Re/datas/DataLake/"

# 공통 고정 변수
now_Year = datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) 

for i in range(4):
#for i in range(276):
    '''공통 수정 변수'''
    now_date = (datetime.utcnow().date() - timedelta(days=i+10))

    # 공통 고정 변수 2
    _, week_num, _ = now_date.isocalendar()
    now_Date = now_date.strftime("%y%m%d")

    directory_player = directory + "players"

    def create_pPlayersFolder():
        if not os.path.exists("%s/Players" % directory_player):
            os.mkdir("%s/Players" % directory_player)
            print("folder created")
        else:
            print("already exists!")

    # players/Players/YYYY
    def create_pPlayersSeasonFolder():
        if not os.path.exists("%s/Players/%s" %(directory_player, now_Year)):
            os.mkdir("%s/Players/%s" %(directory_player, now_Year))
            print("folder created : %s" %now_Year)
        else:
            print("already exists")

    # players/Players/YYYY/week_num
    def create_pPlayersWeekFolder():
        if not os.path.exists("%s/Players/%s/%s" %(directory_player, now_Year, week_num)):
            os.mkdir("%s/Players/%s/%s" %(directory_player, now_Year, week_num))
            print("folder created")
        else:
            print("alreday exists")

    # players/Players/YYYY/week_num/leagueId_players.json
    def create_pPlayersJson():
        db_func = DBfunc()

        #DB server연결 
        db_func.connect_SQL()

        #DB league_id 리스트 반환 
        tmp_leagueId = db_func.read_tmpLeagueId()

        print(tmp_leagueId)

        for i in tmp_leagueId:
            leagueId = i 
            file_path = "%s/Players/%s/%s/%s_players.json" % (directory_player, now_Year, week_num, leagueId)
            data = {'data' : []}
            
            if os.path.exists(file_path):
                print("file exists")
            
            else:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

    # players/Squads
    def create_pSquadsFolder():
        if not os.path.exists("%s/Squads" % directory_player):
            os.mkdir("%s/Squads" % directory_player)
            print("folder created")
        else:
            print("already exists!")

    # players/Squads/YYYY
    def create_pSquadsSeasonFolder():
        if not os.path.exists("%s/Squads/%s" %(directory_player, now_Year)):
            os.mkdir("%s/Squads/%s" %(directory_player, now_Year))
            print("folder created")
        else:
            print("already exists!")

    # players/Squads/YYYY/teamId_Psquad.json
    def create_pSquadsJson():

        db_func = DBfunc()

        #DB server연결 
        db_func.connect_SQL()

        #DB team_id 리스트 반환 
        tmp_teamId = db_func.read_teamId()

        print(tmp_teamId)
        for i in tmp_teamId:
            team_id = i
            file_path = "%s/Squads/%s/%s_Psquad.json" % (directory_player, now_Year, team_id)
            data = {'data' : []}
                
            if os.path.exists(file_path):
                print("file exists")
                
            else:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

    # players/Topscorers
    def create_pTopscorersFolder():
        if not os.path.exists("%s/Topscorers" % directory_player):
            os.mkdir("%s/Topscorers" % directory_player)
            print("folder created")
        else:
            print("already exists!")

    # players/Topscorers/YYYY
    def create_pTopscorersSeasonFolder():
        if not os.path.exists("%s/Topscorers/%s" %(directory_player, now_Year)):
            os.mkdir("%s/Topscorers/%s" %(directory_player, now_Year))
            print("folder created : %s" %now_Year)
        else:
            print("already exists")

    # players/Topscorers/YYYY/ymd_Ptopscorers.json
    def create_pTopscorersJson():
        file_path = "%s/Topscorers/%s/%s_Ptopscorers.json" % (directory_player, now_Year, now_Date)
        data = {'data' : []}
            
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # leagues/YYYY

    directory_leagues = directory + "leagues"

    def create_leaguesSeasonFolder():
        if not os.path.exists("%s/%s" %(directory_leagues, now_Year)):
            os.mkdir("%s/%s" %(directory_leagues, now_Year))
            print("folder created")
        else:
            print("already exists")

    # leagues/YYYY/leagueId_leagueInfo.json
    def create_leaguesJson():

        db_func = DBfunc()

        #DB server연결 
        db_func.connect_SQL()

        #DB league_id 리스트 반환 
        tmp_leagueId = db_func.read_leagueId()

        print(tmp_leagueId)

        for i in tmp_leagueId:
            leagueId = i 
            file_path = "%s/%s/%s_leagueInfo.json" % (directory_leagues, now_Year, leagueId)
            data = {'data' : []}
            
            if os.path.exists(file_path):
                print("file exists")
            
            else:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

    directory_predictions = directory + "predictions"

    #predictions/YYYY
    def create_predictionsSeasonFolder():
        if not os.path.exists("%s/%s" %(directory_predictions, now_Year)):
            os.mkdir("%s/%s" %(directory_predictions, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # predictions/YYYY/ymd_predictions.json
    def create_predictionsJson():
        file_path = "%s/%s/%s_predictions.json" % (directory_predictions, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    directory_standings = directory + "standings"

    # standings/YYYY
    def create_standingSeasonFolder():
        if not os.path.exists("%s/%s" %(directory_standings, now_Year)):
            os.mkdir("%s/%s" %(directory_standings, now_Year))
            print("folder created")
        else:
            print("already exists!")

    # standings/YYYY/ymd_standing.json
    def create_standingJson():
        file_path = "%s/%s/%s_standing.json" % (directory_standings, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    directory_teams = directory + "teams"

    # teams/Info
    def create_teamsInfoFolder():
        if not os.path.exists("%s/Info" % directory_teams):
            os.mkdir("%s/Info" % directory_teams)
            print("folder created")
        else:
            print("already exists!")

    # teams/Info/YYYY
    def create_teamsInfoSeasonFolder():
        if not os.path.exists("%s/Info/%s" %(directory_teams, now_Year)):
            os.mkdir("%s/Info/%s" %(directory_teams, now_Year))
            print("folder created")
        else:
            print("already exists")

    # teams/Info/YYYY/leagueId_Tinfo.json
    def create_teamsInfoJson():
        db_func = DBfunc()

        #DB server연결 
        db_func.connect_SQL()

        #DB league_id 리스트 반환 
        tmp_leagueId = db_func.read_leagueId()

        print(tmp_leagueId)

        for i in tmp_leagueId:
            leagueId = i 
            file_path = "%s/Info/%s/%s_Tinfo.json" % (directory_teams, now_Year, leagueId)
            data = {'data' : []}
            
            if os.path.exists(file_path):
                print("file exists")
            
            else:
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file, indent=4)

    # teams/Statistics
    def create_teamsStatisticsFolder():
        if not os.path.exists("%s/Statistics" % directory_teams):
            os.mkdir("%s/Statistics" % directory_teams)
            print("folder created")
        else:
            print("already exists!")

    # teams/Statistics/YYYY
    def create_teamsStatisticsSeasonFolder():
        if not os.path.exists("%s/Statistics/%s" %(directory_teams, now_Year)):
            os.mkdir("%s/Statistics/%s" %(directory_teams, now_Year))
            print("folder created")
        else:
            print("already exists")


    def create_teamsStatisticsJson():
        file_path = "%s/Statistics/%s/%s_Tstats.json" % (directory_teams, now_Year, now_Date)
        data = {'data' : []}

        if os.path.exists(file_path):
            print("file exists")

        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    create_pPlayersFolder()
    create_pPlayersSeasonFolder()
    create_pPlayersWeekFolder()
    create_pPlayersJson()

    create_pSquadsFolder()
    create_pSquadsSeasonFolder()
    create_pSquadsJson()

    create_pTopscorersFolder()
    create_pTopscorersSeasonFolder()
    create_pTopscorersJson()

    create_leaguesSeasonFolder()
    create_leaguesJson()

    create_predictionsSeasonFolder()
    create_predictionsJson()

    create_standingSeasonFolder()
    create_standingJson()

    create_teamsInfoFolder()
    create_teamsInfoSeasonFolder()
    create_teamsInfoJson()

    create_teamsStatisticsFolder()
    create_teamsStatisticsSeasonFolder()
    create_teamsStatisticsJson()