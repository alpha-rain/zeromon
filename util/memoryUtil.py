import datetime
import psutil
import cpuinfo
import platform
import json
import re
import tojson


def info():
    jsondata = '"memory":{"ram":{'
    jsondata += '"info":{},'
    jsondata += virtualMemoryPerformance('usage')
    jsondata += '}}'
    return jsondata

def virtualMemoryPerformance(label):
    virtualMemoryStats  = psutil.virtual_memory()
    
    jsondata = '"'
    jsondata += label
    jsondata += '":{'
    jsondata += tojson.toJson(virtualMemoryStats._fields,virtualMemoryStats)
    jsondata += '}'
    
    return jsondata