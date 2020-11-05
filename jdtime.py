#-*- coding:utf-8 -*-

import time
from datetime import datetime
import requests
import json
# import win32api

def getTime():
    url = 'https://a.jd.com//ajax/queryServerData.html'
    ret = requests.get(url).text
    js = json.loads(ret)

    return float(js["serverTime"])/1000


def get_jd_times():

    resp = requests.session().get('https://item.jd.com/')
    ts = resp.headers.get('date')
    # 转为北京时间
    ltime = time.strptime(ts[5:25], '%d %b %Y %H:%M:%S')
    ttime = time.localtime(time.mktime(ltime) + 8 * 60 * 60)
    times = time.mktime(ttime)
    return time.localtime(times)

if __name__ == '__main__':
    # setSystemTime()
    # while True:
    #     print("京东时间:%s"%(datetime.fromtimestamp(getTime())))
    #     print("本地时间:%s\n"%(datetime.strftime(datetime.today(),'%Y-%m-%d %H:%M:%S.%f',)))
    #
    #     # 1.263032

    from config import global_config
    while True:
        buy_time = datetime.strptime(global_config.getRaw('config', 'buy_time'), "%Y-%m-%d %H:%M:%S.%f")
        now_time = datetime.fromtimestamp(getTime())
        print(buy_time)
        print(now_time)

        if now_time >= buy_time:
            print("抢购")
            break
        else:
            print("时间未到")
            time.sleep(0.05)

    # print("京东时间:%s" % (datetime.fromtimestamp(getTime())))
    # print(time.strftime("%Y-%m-%d %H:%M:%S",get_jd_times()))
    # print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))