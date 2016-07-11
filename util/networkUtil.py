import datetime
import psutil
import cpuinfo
import platform
import json
import re
# import tojson

def info():
    jsondata = '"network":{"info":{'
    jsondata += '},"usage":{'
    jsondata += networkConnectionsInfo()
    jsondata += '}}'
    return jsondata

def networkConnectionsInfo():
    networkConnections = psutil.net_connections()
    jsondata = toJsonArray(networkConnections, 'network-connections', True, True); 
    return jsondata


def tupletojson(fields,dataString = False,isnumeric = False):
    jsondata = '['
    fieldsLength = len(fields);
    fieldCount = 0
    for field in fields:
        if(dataString and (isnumeric == False)):
            jsondata += '"'
        elif(isnumeric):
            if(isinstance(field,float) == False) and (isinstance(field,int) == False):
                jsondata += '"'
        jsondata +=str(field)
        if(dataString and (isnumeric == False)):
            jsondata += '"'
        elif(isnumeric):
            if(isinstance(field,float) == False) and (isinstance(field,int) == False):
                jsondata += '"'
        fieldCount +=1
        if fieldsLength != fieldCount:
            jsondata += ','   
    jsondata += ']'
    return jsondata
    
def toJson(fields,data,dataString = False,isnumeric = False):
    jsondata = ''
    fieldsLength = len(fields);
    fieldCount = 0
    for field in fields:
        jsondata += '"'
        jsondata += field
        jsondata += '":'
        # print( type(data[fieldCount]))
        if(isinstance(data[fieldCount], tuple)):
            jsondata += tupletojson(data[fieldCount],dataString,isnumeric)
        else:
            if(dataString and (isnumeric == False)):
                jsondata += '"'
            elif(isnumeric):
                tests = str(data[fieldCount]).isnumeric()
                # if(unicode(str(data[fieldCount])).isnumeric() == False):
                if(isinstance(data[fieldCount],float) == False) and (isinstance(data[fieldCount],int) == False):
                    jsondata += '"'
            if(field == 'family'):
                jsondata += str(data[fieldCount].real)
            else:
                jsondata += str(data[fieldCount])
            if(dataString and (isnumeric == False)):
                jsondata += '"'
            elif(isnumeric):
                if(isinstance(data[fieldCount],float) == False) and (isinstance(data[fieldCount],int) == False):
                    jsondata += '"'
        fieldCount +=1
        if fieldsLength != fieldCount:
            jsondata += ','   
    return jsondata

def toJsonArray(datas, name,dataString = False,isnumeric = False):
    jsondata = '"'
    jsondata += name
    jsondata += '":[' 
    dataLength = len(datas);
    dataCount = 0
    for data in datas:
        jsondata += '{'
        jsondata += toJson(data._fields,data,dataString,isnumeric)    
        dataCount += 1
        if dataLength != dataCount:
            jsondata += '},' 
        
    jsondata += '}]'
    return jsondata