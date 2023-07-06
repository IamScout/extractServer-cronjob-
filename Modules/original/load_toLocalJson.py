import json
import os
import datetime


def load_standingJson(tmp_data, league_id):
    nowDate = datetime.datetime.now().date().strftime("%y%m%d")
    
    directory = os.path.join(os.path.dirname(__file__), "..", 'datas', 'DataLake', 'standings')
    print(directory)
    with open("%s/%s_%d_standing.json" % (directory, nowDate, league_id), "r") as json_file:
        data = json.load(json_file)
     
    
    data['data'].append(tmp_data)

    print(tmp_data)

    with open("%s/%s_%d_standing.json" % (directory, nowDate, league_id), "w") as json_file:
        json.dump(data, json_file, indent=4)
        print("sucksex")
    