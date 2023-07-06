# 실행 완료
# 다시 돌릴 필요 없음

import os

# 디렉토리
# directory = os.path.join(os.path.dirname(__file__), "../datas/DataLake")

# 도훈's 디렉토리
directory = "/etl/ETLServer_Re/datas/DataLake"

# fixtures
def create_fixturesBaseFolder():
	if not os.path.exists("%s/fixtures" %directory):
		os.mkdir("%s/fixtures" %directory )
		print("folder created")
	else:
		print("already exists!")

# leagues
def create_leaguesBaseFolder():
	if not os.path.exists("%s/leagues" %directory):
		os.mkdir("%s/leagues" %directory)
		print("folder created")
	else:
		print("already exists!")

# players
def create_playersBaseFolder():
	if not os.path.exists("%s/players" %directory):
		os.mkdir("%s/players" %directory)
		print("folder created")
	else:
		print("already exists!")

# predictions
def create_predictionsBaseFolder():
	if not os.path.exists("%s/predictions" %directory):
		os.mkdir("%s/predictions" %directory)
		print("folder created")
	else:
		print("already exists!")

# standings
def create_standingsBaseFolder():
	if not os.path.exists("%s/standings" %directory):
		os.mkdir("%s/standings" %directory)
		print("folder created")
	else:
		print("already exists!")

# teams
def create_teamsBaseFolder():
	if not os.path.exists("%s/teams" %directory):
		os.mkdir("%s/teams" %directory)
		print("folder created")
	else:
		print("already exists!")

create_fixturesBaseFolder()
create_leaguesBaseFolder()
create_playersBaseFolder()
create_predictionsBaseFolder()
create_standingsBaseFolder()
create_teamsBaseFolder()