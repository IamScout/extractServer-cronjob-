import os
import json
import datetime
from httpRes_func import *

nowDate = datetime.now().date().strftime("%Y_%m_%d")
directory = os.path.join(os.path.dirname(__file__), 'datas', 'Logs')

def convertToJson(resTime, crudOpt, date, time, http_Status):

    tmpDict = {}
    tmpDict['responseTime'] = resTime
    tmpDict['crudOption'] = crudOpt
    tmpDict['Date'] = date
    tmpDict['Time'] = time
    tmpDict['httpStatus'] = http_Status

    return tmpDict


def writeToJson(httpStatusDict):
    existingFile = os.listdir(directory)
    with open("%s" %(existingFile), "w") as f:
        json.dump(httpStatusDict, f)
    f.close()

startTime = time.time()
baseStatus = re.get(url = getBaseInfoUrl, headers = headers)
respTime = resTime(startTime)

status = baseStatus.headers

getUrl()
crudOpt = getCrudOpt()
tmpDate = getTimeStamp()[0]
tmpTime = getTimeStamp()[1]
tmpHttpStatus = httpStatus()

dataToJson = convertToJson(respTime,crudOpt,tmpDate,tmpTime,tmpHttpStatus)

writeJson = writeToJson(dataToJson)







