from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Courses(request):
    return HttpResponse('This is course page.')


def About(request):
    return render(request, 'about.html', {'i_d': request.GET})


def Index(request):
    data = [{
        "id": 1,
        "name": 'habib',
        "title": 'Engineer'
    }, {
        "id": 2,
        "name": 'karim',
        "title": 'Doctor'
    }]
    return render(request, 'index.html', {'data': data})