import requests
import re
import os
def getStation():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9098'
    response = requests.get(url,verify=True)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)  # \U + 十六进制 表示与unicode编码相关
    # “\u”后的16进制字符串是相应汉字的utf-16编码。python里decode()和encode()为我们提供了解码和编码的方法。
    stations =dict((stations))
    stations = str(stations)
    write(stations)
def write(stations):
    file = open('stations.text','w',encoding='utf_8_sig')
    file.write(stations)
    file.close()
def read():
    file = open('stations.text','r',encoding='utf_8_sig')
    data = file.readline()
    file.close()
    return data
def isStations():
    isStation = os.path.exists('stations.text')
    return isStation
