from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
def first(request):
    res=isinstance(request,HttpRequest)
    print(res)
    print(request.method)
    return  HttpResponse ('helloworld')
def secondview(request):
    return HttpResponse ('we are learning django')
def thirdview(request):
    return HttpResponse('i love u sindhu forever')