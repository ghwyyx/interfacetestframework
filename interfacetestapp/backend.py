# @author='guhao'
# @time:2019/09/03 19:30:00

import requests,json
from .models import InterfaceModel
from datetime import datetime


def resultrequest(requesttype,requesturl,requestbody):
    if requesttype == 'GET':
        newbody = geturldata(requestbody)
        getdata = requests.get(requesturl,newbody)
        return getdata.json()
    elif requesttype == 'POST':
        httptype = requesturl.split(':')[0]
        if httptype == 'http':
            header = {"Content-Type":"application/json;charset=UTF-8"}
            responsdata = requests.post(url=requesturl,headers=header, data=requestbody)
            return responsdata.json()
        elif httptype == 'https':
            newdata = 'data='.__add__(requestbody)
            header = {"Content-Type":"application/x-www-form-urlencoded"}
            httpsresponse = requests.post(url=requesturl,headers=header,data=newdata,verify=False)
            return httpsresponse.json()


def geturldata(data):
    keyandvalue = data.replace(',','&')
    newkv = keyandvalue.replace(':','=')
    return newkv

def my_save(*args):
    InterfaceModel.objects.create(http_method=args[0],url=args[1],request_body=json.dumps(args[2]),interface_name=args[3])


def getDataFromMongoDB():
    dataModel = InterfaceModel.objects.all()
    jsonArray = []
    for data in dataModel:
        method_name = data.interface_name
        http_method=data.http_method
        url = data.url
        request_body = json.loads(data.request_body)
        tmpData = {"methodname":method_name,"methodtype":http_method,"methodurl":url,"methodbody":request_body}
        jsonArray.append(tmpData)
    return {"total": InterfaceModel.objects.count(), "rows": jsonArray}

def dealmanyreqests(data):
    tmpArray = []
    for req in data:
        tmpData = req.split(';')
        print(resultrequest(tmpData[1], tmpData[2], tmpData[3]))
        secondTmpData = resultrequest(tmpData[1], tmpData[2], tmpData[3])
        print(datetime.now())
        tmpDictData = {'executeDate': datetime.now(), 'executeResult': secondTmpData['header']['repmsg']}
        tmpArray.append(tmpDictData)
    return tmpArray