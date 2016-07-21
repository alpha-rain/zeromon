import sys
import json
import calendar
import time
import comms

sys.path.insert(0, './util')
import osUtil
import cpuUtil
import memoryUtil
import diskUtil
import networkUtil

VERSION = '1.0'

def new_system_data():
    """makes json string with system performance data to send out"""
    jsondata = '{' + packet_info()
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

def packet_info():
    """gives info about the packet version and time packet made/sent"""
    jsondata = '"packet-info":{"version":"' + VERSION + '","time":'
    jsondata += str(calendar.timegm(time.gmtime()))
    jsondata += '}'
    return jsondata

def write_file(data):
    target = open('testout.json', 'w')
    target.write(data)
    target.close()

def schedule(comm):
    print('ow')
    new_system_data()
    time.sleep(1)
    while True:
        data = new_system_data()
        write_file(data)
        jsondata = json.loads(data)
        comm.send(jsondata)
        time.sleep(5)
    

comm = comms.manage()
with open('config.json') as json_file:
    json_data = json.load(json_file)
    commsConfig = json_data['endpoint-locations']
    comm.config(commsConfig)
schedule(comm)