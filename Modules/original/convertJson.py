'''
[변경] convertJson > convert_toJson
[1] json 파일에 적재할 log 정보들을 딕셔너리의 형태로 정리
'''

# [변경] convertToJson > convert_toJson
# [변경] resTime, crudOpt, http_Status > response_time, crud_option, http_status
def convert_toJson(response_time, crud_option, uri_info, date, time, http_status):

    tmp_dict = {}
    tmp_dict['response_time'] = response_time
    tmp_dict['crud_option'] = crud_option
    tmp_dict['url'] = uri_info[0]
    tmp_dict['parameter'] = uri_info[1]
    tmp_dict['date'] = date
    tmp_dict['time'] = time
    tmp_dict['http_status'] = http_status

    return tmp_dict