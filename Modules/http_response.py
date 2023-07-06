'''
[Code Explanation]
- API request의 요청 정보를 1차 가공하여 각기 반환하는 함수 집합
- get_uriInfos와 get_timeStamp는 len 2의 리스트 형태로 데이터 반환

[Need to Know]
- 
'''

import time
from datetime import datetime

# resTime > get_responseTime
def get_responseTime(start_time):
        response_time = (time.time() - start_time)
        return response_time

# getUrl > get_parameter
# 리스트의 형태로 정보 반환
def get_uriInfos(uri):
        url = uri[ : uri.index('?')]
        parameter = uri[uri.index('?') : ]
        uri_info = [url, parameter]
        return uri_info

# getCrudOpt > get_crudOption
def get_crudOption(status):
        crud_option = status['Access-Control-Allow-Methods']
        crud_option = crud_option[:crud_option.index(',')]
        return crud_option

# getTimeStamp > get_timeStamp
def get_timeStamp(status):
        date_str = status['date']
        date_format = "%a, %d %b %Y %H:%M:%S %Z"
        date_obj = datetime.strptime(date_str, date_format)
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        hour = date_obj.hour
        minute = date_obj.minute
        second = date_obj.second
        now_date = str(year) + "_" + str(month) + "_" + str(day)
        now_time = str(hour) + "_" + str(minute) + "_" + str(second)
        time_stamp = [now_date, now_time]
        return time_stamp

# httpStatus > get_httpStatus
def get_httpStatus(status):
        http_status = status.status_code
        return http_status