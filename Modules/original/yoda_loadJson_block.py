'''
[변경] yoda_loadJson_block > load_json
[1] API request의 log 데이터를 가공된 형태로 받아 json 파일에 적재
'''

import json, os
from datetime import datetime

# [변경] loadMonitoringJson > load_json
# [변경] tmpList > tmp_list
def load_json(tmp_list):
    
    # [변경] nowDate > now_date
    now_date = datetime.utcnow().date().strftime("%Y_%m_%d")
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'Logs')

    with open("%s/%s/%s.json" % (directory, now_date, now_date), "r") as json_file:
        data = json.load(json_file)

    data['data'].append(tmp_list)

    with open("%s/%s/%s.json" % (directory, now_date, now_date), "w") as json_file:
        json.dump(data, json_file, indent=4)