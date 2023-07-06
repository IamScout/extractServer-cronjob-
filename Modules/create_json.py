'''
[Code Explanation]
- API request 요청 정보 딕셔너리를 log 폴더 내에 json 파일로 저장
- http_response 내부에 import된 모듈을 공유

[Need to Know]
- 
'''

import os
import json
from http_response import *

now_date = datetime.utcnow().date().strftime("%Y_%m_%d")
directory = os.path.join(os.path.dirname(__file__), 'datas', 'Logs')

def load_toJson(tmp_dict):
    existing_file = f"{os.listdir(directory)}/{now_date}/{now_date}.json"
    with open("%s" %(existing_file), "w") as file:
        json.dump(tmp_dict, file)
    file.close()


if __name__ == "__main__":
    tmp_dict = {'test' : "success"}
    load_toJson(tmp_dict)