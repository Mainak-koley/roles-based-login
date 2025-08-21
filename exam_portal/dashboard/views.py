from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def TestView(request):
    return HttpResponse("test server")