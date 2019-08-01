from django.shortcuts import render
from .backend import resultrequest,my_save
import json

# Create your views here.
def simple_interface(requests):
    if requests.method == 'GET':
        return render(requests, 'index.jsp')
    elif requests.method == 'POST':
        print('111111111111111111111111111')
        requestselect = requests.POST['requestselect']
        requesturl = requests.POST['requestsurl']
        requestbody = requests.POST['requestvalue']
        expectnumber = requests.POST['input_number']
        checkvalue=requests.POST.getlist('saveinput')
        if len(checkvalue) == 1:
            my_save(requestselect,requesturl,requestbody,expectnumber)
            print(requestselect,requesturl,requestbody,expectnumber)
        else: print('不进行数据存储')
        result = resultrequest(requesttype=requestselect,requesturl=requesturl,requestbody=requestbody,returntotal=expectnumber)
        context = {'result':result}
        return render(requests, 'c.asp', context)

def showinterfacelist(requests):
    return render(requests,'b.asp')

def showinterfaceresult(requests):
    return render(requests,'c.asp')