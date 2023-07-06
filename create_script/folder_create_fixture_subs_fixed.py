# Firture 관련 폴더 생성 스크립트

# 모듈 불러오기
import os, json
from datetime import datetime, timedelta

# 공통 디렉토리
# directory = os.path.join(os.path.dirname(__file__), '../datas/DataLake/fixtures')

# 도훈's 디렉토리
directory = "/etl/ETLServer_Re/datas/DataLake/fixtures"

# 공통 고정 변수
now_Year = datetime.utcnow().date().strftime("%Y")
now_Year = str(int(now_Year) - 1) 

# 공통 수정 변수
# 23.05.13 기준 +4

for i in range(3):
#for i in range(276):
    now_Date = (datetime.utcnow().date() - timedelta(days=i+5)).strftime("%y%m%d")

    # fixture/events
    def create_eventsFolder():
        if not os.path.exists("%s/events" %directory):
            os.mkdir("%s/events" %directory)
            print("folder created")
        else:
            print("already exists!")

    # fixture/events/YYYY
    def create_eventsSeasonFolder():
        if not os.path.exists("%s/events/%s" %(directory, now_Year)):
            os.mkdir("%s/events/%s" %(directory, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # fixture/events/YYYY/ymd_events.json
    def create_eventsJson():
        file_path = "%s/events/%s/%s_events.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # fixtures/fixtures
    def create_fixturesFolder():
        if not os.path.exists("%s/fixtures" %directory):
            os.mkdir("%s/fixtures" %directory)
            print("folder created!")
        else:
            print("already exists!")

    # fixtures/fixtures/YYYY
    def create_fixturesSeasonFolder():
        if not os.path.exists("%s/fixtures/%s" %(directory, now_Year)):
            os.mkdir("%s/fixtures/%s" %(directory, now_Year))
            print("folder created")
        else:
            print("already exists!")

    # fixtures/fixtures/YYYY/ymd_fixture.json
    def create_fixturesJson():
        file_path = "%s/fixtures/%s/%s_fixture.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # fixtures/Pstatistics
    def create_fixturesPStatsFolder():
        if not os.path.exists("%s/Pstatistics" %directory):
            os.mkdir("%s/Pstatistics" %directory)
            print("folder created")
        else:
            print("already exists!")

    # fixtures/Pstatistics/YYYY
    def create_fixturesPStatsSeasonFolder():
        if not os.path.exists("%s/Pstatistics/%s" %(directory, now_Year)):
            os.mkdir("%s/Pstatistics/%s" %(directory, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # fixtures/Pstatistics/YYYY/ymd_Pstatistics.json
    def create_fixturesPStatsJson():
        file_path = "%s/Pstatistics/%s/%s_Pstatistics.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # fixtures/Tstatistics
    def create_fixturesTstatsFolder():
        if not os.path.exists("%s/Tstatistics" %directory):
            os.mkdir("%s/Tstatistics" %directory)
            print("folder created")
        else:
            print("already exists!")

    # fixtures/Tstatistics/YYYY
    def create_fixturesSeasonTstatsFolder():
        if not os.path.exists("%s/Tstatistics/%s" %(directory, now_Year)):
            os.mkdir("%s/Tstatistics/%s" %(directory, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # fixtures/Tstatistics/YYYY/ymd_Tstatistics.json
    def create_fixturesTstatsJson():
        file_path = "%s/Tstatistics/%s/%s_Tstatistics.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # fixtures/H2h
    def create_h2hFolder():
        if not os.path.exists("%s/H2h" %directory):
            os.mkdir("%s/H2h" %directory)
            print("folder created")
        else:
            print("already exists!")

    # fixtures/H2h/YYYY
    def create_h2hSeasonFolder():
        if not os.path.exists("%s/H2h/%s" %(directory, now_Year)):
            os.mkdir("%s/H2h/%s" %(directory, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # fixtures/H2h/YYYY/ymd_h2h.json
    def create_h2hJson():
        file_path = "%s/H2h/%s/%s_h2h.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
            
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    # fixtures/lineups
    def create_lineUpsFolder():
        if not os.path.exists("%s/lineups" %directory):
            os.mkdir("%s/lineups" %directory)
            print("folder created")
        else:
            print("already exists!")

    # fixtures/lineups/YYYY
    def create_lineUpsSeasonFolder():
        if not os.path.exists("%s/lineups/%s" %(directory, now_Year)):
            os.mkdir("%s/lineups/%s" %(directory, now_Year))
            print("folder created! : %s" %now_Year)
        else:
            print("already exists")

    # fixtures/lineups/YYYY/ymd_lineUps.json
    def create_lineUpsJson():
        file_path = "%s/lineups/%s/%s_lineUps.json" % (directory, now_Year, now_Date)
        data = {'data' : []}
        
        if os.path.exists(file_path):
            print("file exists")
        
        else:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
                print('json file created!')

    create_eventsFolder()
    create_eventsSeasonFolder()
    create_eventsJson()

    create_fixturesFolder()
    create_fixturesSeasonFolder()
    create_fixturesJson()

    create_fixturesPStatsFolder()
    create_fixturesPStatsSeasonFolder()
    create_fixturesPStatsJson()

    create_fixturesTstatsFolder()
    create_fixturesSeasonTstatsFolder()
    create_fixturesTstatsJson()

    create_h2hFolder()
    create_h2hSeasonFolder()
    create_h2hJson()

    create_lineUpsFolder()
    create_lineUpsSeasonFolder()
    create_lineUpsJson()