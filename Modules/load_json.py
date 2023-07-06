'''
[Code Explanation]
- API reques의 log 정보를 담은 json 파일의 생성 및 수정

[Need to Know]
- 
'''

import json, os
from datetime import datetime

# loadMonitoringJson > load_json
# tmpList > tmp_list
def load_json(tmp_list):
    
    # nowDate > now_date
    now_date = datetime.utcnow().date().strftime("%Y_%m_%d")
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'Logs')

    with open("%s/%s/%s.json" % (directory, now_date, now_date), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_list)

    with open("%s/%s/%s.json" % (directory, now_date, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)