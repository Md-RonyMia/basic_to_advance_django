from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Courses(request):
    return HttpResponse('This is course page.')


def About(request):
    return HttpResponse('This is about page.')

def Index(request):
    data={'name':'karim','age':18,'lst':['python','is','best']}
    return render(request,'index.html',data)