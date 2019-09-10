# @author='guhao'
# @time:2019/09/03 19:30:00

from django.shortcuts import render
from .backend import resultrequest,my_save,getDataFromMongoDB,dealmanyreqests
from django.http import JsonResponse


# Create your views here.
# 发送接口请求
def simple_interface(requests):
    if requests.method == 'GET':
        return render(requests, 'index.html')
    elif requests.method == 'POST':
        requestselect = requests.POST['requestselect']
        requesturl = requests.POST['requestsurl']
        requestbody = requests.POST['requestvalue']
        interfacename = requests.POST['interfacename']
        checkvalue=requests.POST.getlist('saveinput')
        if len(checkvalue) == 1:
            my_save(requestselect,requesturl,requestbody,interfacename)
        else: print('不进行数据存储')
        result = resultrequest(requesttype=requestselect,requesturl=requesturl,requestbody=requestbody)
        context = {'result':result}
        return render(requests, 'c.html', context)

# 展示所有已存储的接口数据
def showinterfacelist(requests):
    # getDataFromMongoDB()
    return render(requests,'b.html')

# 从数据库中查询所有接口数据
def getinterfacelistdata(requests):
    return JsonResponse(getDataFromMongoDB())

# 展示接口请求结果
def showinterfaceresult(requests):
    return render(requests,'c.html')

# 批量处理请求
def dealallrequests(requests):
    if requests.method == 'POST':
        ttData = {'total':len(requests.POST.getlist('stringData[]')),'rows':dealmanyreqests(requests.POST.getlist('stringData[]'))}
        return JsonResponse(ttData)
    elif requests.method == 'GET':
        return JsonResponse({'status':200})

# 展示批处理结果
def showallrequests(requests):
    return render(requests, 'd.html')