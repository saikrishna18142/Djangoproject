from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addition(request):
    if request.method == 'GET':
        return render(request,'calculator/addition.html')
    if request.method =='POST':
        print('request.POST')
        v1=int (request.POST['t1'])
        v2=int(request.POST['t2'])
        if 'add' in request.POST:
            res=v1+v2
            action='Addition'
        elif 'sub' in request.POST:
            res=v1-v2
            action='substraction'
        elif 'multi' in request.POST:
            res=v1*v2
            action='multiplication'
        else:
            res=v1/v2
            action='DIVISION'
        #return HttpResponse('Addition'+str(res))
        return render(request,'calculator/addition.html',{'result' : res,'action':action,'msg':'we are truly good students'})
    
      
def mathtable(request):
    if request.method =='GET':
        return render(request,'calculator/mtable.html')
    if request.method == 'POST':
        num=int(request.POST['t1'])
        output=[]
        for i in range(1,11):
            output.append(str(i)+' * '+str(num)+' = '+str(i*num))
        return render(request,'calculator/mtable.html',{'table':output})