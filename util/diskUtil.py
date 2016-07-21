import datetime
import psutil
# import cpuinfo
import platform
import json
import re
import tojson

def info():
    jsondata = r'{"info":{},' + diskPerformance('usage') + '}'
    # jsonEncode = json.dumps(jsondata)
    jsondata = jsondata.replace('\\','\\\\')
    jsonDiskDevs = json.loads(jsondata)
    for jsonDiskDev in jsonDiskDevs['usage']:
        if(jsonDiskDev['opts'] == 'cdrom'):
            continue
        mountpoint = jsonDiskDev['mountpoint']
        diskUsage = '{' + diskInfoPerformance(mountpoint) + '}'
        diskUsageJson = json.loads(diskUsage)#.decode('string_escape'))
        jsonDiskDev['diskinfo']=diskUsageJson
    data = json.dumps(jsonDiskDevs)
    data = data[:-1]
    data = data[1:]
    data = '"disk":{' + data + '}'
    return data

def diskPerformance(label):
    disks = psutil.disk_partitions()
    jsondata = tojson.toJsonArray(disks, label, True);   
    
    return jsondata;

def diskInfoPerformance(path):
    diskInfo = psutil.disk_usage(path)
    jsondata = tojson.toJson(diskInfo._fields,diskInfo)
    return jsondata