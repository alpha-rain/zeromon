import psutil
import platform
import json
import re
import tojson

def info():
    jsondata = '"os":{'
    jsondata += '"system":"'
    jsondata += platform.system()
    jsondata += '","network-name":"'
    jsondata += platform.node()
    jsondata += '","release":"'
    jsondata += platform.release()
    jsondata += '","version":"'
    jsondata += platform.version()
    jsondata += '","arch":"'
    jsondata += platform.machine()
    jsondata += '","boot-time":'
    jsondata += str(psutil.boot_time())
    jsondata += ','
    jsondata += usersInfo()
    os = platform.system()
    rl = platform.release()
    vs = platform.version()
    mh = platform.machine()
    un = platform.uname()
    nd = platform.node()
    jsondata += '}'
    
    
    return jsondata

def usersInfo():
    users = psutil.users()
    jsondata = tojson.toJsonArray(users,'users',True, True)
    return jsondata