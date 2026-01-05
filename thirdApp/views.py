from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def sendtemplate(request):
   # return  HttpResponse('saikrishna Chowdary')
    return render(request,'third.html')