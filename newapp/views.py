from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Courses(request):
    return HttpResponse('This is course page.')


def About(request):
    if request.method=='GET':
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