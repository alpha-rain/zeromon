import datetime
import psutil
import cpuinfo
import platform
import json
import re
import tojson

def info():
    cpuInfo = cpuinfo.get_cpu_info()

    jsondata = '"cpu":{"info":{'
    jsondata += '"name":"'
    jsondata += cpuInfo['brand']
    jsondata += '","architecture":"'
    jsondata += cpuInfo['arch']
    jsondata += '","speed":"'
    jsondata += cpuInfo['hz_advertised']
    jsondata += '","cores":{"real":'
    jsondata += str(psutil.cpu_count() - psutil.cpu_count(logical=False))
    jsondata += ',"hyper":'
    jsondata += str(psutil.cpu_count(logical=False))
    jsondata += '}},'
    jsondata +=cpuPerformance('usage')
    jsondata += '}'
    return jsondata

def cpuPerformance(label): 
    cpuStats = psutil.cpu_times_percent(interval=0, percpu=True)
    
    jsondata = tojson.toJsonArray(cpuStats, label);    
    
    return jsondata