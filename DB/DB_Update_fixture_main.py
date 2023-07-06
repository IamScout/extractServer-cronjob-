# db 열고
# fixture id 중 date의 오늘 날짜를 list 로 반환
# 반환 받은 list로 api call -> rep 
# 필요한 데이터로 변환
# db 업데이트

from ETLServer.Modules.db_function import * 
from ETLServer.Modules.api_func import *
from datetime import datetime, timedelta

# api_keys = "a68636f8f2c18511179c56f15e95080c"
api_keys = "a86d420d0d8840c8e722e16cf9742f7b"
# api_keys = "e6b9fb7ce7a7ad7b239595f76e546384"

db_func = DBfunc()
api_func = ApiUpdateFixture()

db_func.connect_SQL()

today_date = datetime.utcnow().date().strftime('%Y-%m-%d')
yesterday = (datetime.utcnow().date() - timedelta(days=1)).strftime("%Y-%m-%d")

fixture_list = db_func.read_fixtureId(yesterday)

update_data = api_func.update_todayRoundFixture(fixture_list, api_keys)

db_func.update_fixture(update_data)








