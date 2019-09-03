import requests,json
from .models import InterfaceModel


def resultrequest(requesttype,requesturl,requestbody,returntotal):
    if requesttype == 'GET':
        newbody = geturldata(requestbody)
        getdata = requests.get(requesturl,newbody)
        try:
            if int(returntotal) == len(getdata.json()) or returntotal == '':return getdata.json()
        except:return '返回参数与预期不符'
    elif requesttype == 'POST':
        httptype = requesturl.split(':')[0]
        if httptype == 'http':
            header = {"Content-Type":"application/json;charset=UTF-8"}
            responsdata = requests.post(url=requesturl,headers=header, data=requestbody)
            # return responsdata.json()
            try:
                if returntotal == '':
                    return responsdata.json()
                elif int(returntotal) == len(responsdata.json()):
                    return responsdata.json()
            except:return '返回参数与预期不符'
        elif httptype == 'https':
            newdata = 'data='.__add__(requestbody)
            print(newdata)
            header = {"Content-Type":"application/x-www-form-urlencoded"}
            httpsresponse = requests.post(url=requesturl,headers=header,data=newdata,verify=False)
            newresponsedata = httpsresponse.json()
            # return newresponsedata
            try:
                if returntotal == '':
                    return newresponsedata
                elif int(returntotal) == len(httpsresponse.json()):
                    return newresponsedata
            except:return '返回参数与预期不符'


def geturldata(data):
    keyandvalue = data.replace(',','&')
    newkv = keyandvalue.replace(':','=')
    return newkv

def my_save(*args):
    InterfaceModel.objects.create(http_method=args[0],url=args[1],request_body=json.dumps(args[2]),expect_num=args[3])


def getDataFromMongoDB():
    dataModel = InterfaceModel.objects.all()
    print(type(dataModel),dataModel[0].url,json.loads(dataModel[0].request_body))
    print(InterfaceModel.objects.count())
    jsonArray = []
    for data in dataModel:
        http_method=data.http_method
        url = data.url
        request_body = json.loads(data.request_body)
        tmpData = {"methodtype":http_method,"methodurl":url,"methodbody":request_body}
        jsonArray.append(tmpData)
    print(type(json.dumps({"total": InterfaceModel.objects.count(), "rows": jsonArray})))
    return {"total": InterfaceModel.objects.count(), "rows": jsonArray}
