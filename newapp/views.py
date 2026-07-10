from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

# Create your views here.
def Courses(request):
    return HttpResponse('This is course page.')


def About(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        return render(request,'about.html',{'name':username,'email':email})
    else:
        return render(request,'about.html')
         
        
        
         

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


def user_form(request):
        return render(request,'form.html')


def Django_form(request):
    std=Student.objects.all()
    return render(request, 'django_form.html',{'data':std})

          