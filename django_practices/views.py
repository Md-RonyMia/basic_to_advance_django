from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("This is home page")

