import psutil
import json
import calendar
import time
import sys
import comms

sys.path.insert(0, './util')
import osUtil
import cpuUtil
import memoryUtil
import diskUtil
import networkUtil


version = '1.0'

def newSystemData():
    jsondata =  '{' + packetInfo()
    jsondata += ',"pc-details":{'
    jsondata += osUtil.info()
    jsondata += ','
    jsondata += cpuUtil.info()
    jsondata += ','
    jsondata += memoryUtil.info()
    jsondata += ','
    jsondata += diskUtil.info()
    jsondata += ','
    jsondata += networkUtil.info()     
    jsondata += '}}'
    return jsondata

def packetInfo():
    jsondata = '"packet-info":{"version":"' + version + '","time":'
    jsondata += str(calendar.timegm(time.gmtime()))
    jsondata += '}'
    return jsondata

def schedule(comm):
    print('ow')
    newSystemData()
    time.sleep(1)
    while True:
        jsondata = json.loads(newSystemData())
        comm.send(jsondata)
        time.sleep(5)
    

comm = comms.manage()
with open('config.json') as json_file:
    json_data = json.load(json_file)
    commsConfig = json_data['endpoint-locations']
    comm.config(commsConfig)
schedule(comm)
schedule()
newSystemData()