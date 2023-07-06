import requests as re
import time
from datetime import datetime


def resTime(res):
        # responseTime = round((time.time() - startTime),4)

        responseTime = (time.time() - res)
        #응답시간 변수 이름 responeTime
        return responseTime

def getUrl(getBaseInfoUrl):
        endPointUrl = getBaseInfoUrl[:getBaseInfoUrl.index('?')]
        return endPointUrl

def getCrudOpt(status):
        crudOption = status['Access-Control-Allow-Methods']
        crudOption = crudOption[:crudOption.index(',')]
        return crudOption


def getTimeStamp(status):
        dateString = status['date']
        dateObj = datetime.strptime(dateString, "%a, %d %b %Y %H:%M:%S %Z")
        year = dateObj.year
        month = dateObj.month
        day = dateObj.day
        # gmt gg 
        hour = dateObj.hour
        minute = dateObj.minute
        second = dateObj.second

        nowDate = str(year) + "_" + str(month) + "_" + str(day)
        nowTime = str(hour) + "_" + str(minute) + "_" + str(second)

        finalList = [nowDate, nowTime]

        #return nowDate, nowTime
        return finalList

def httpStatus(status):
        httpStatus = status.status_code
        return httpStatus


def test():
        print("hihi")

