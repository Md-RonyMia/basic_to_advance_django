from django.shortcuts import render

# Create your views here.
from .forms import UserCreate

def HOME(request):
    if request.method == 'POST':
        form=UserCreate(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            form.save(commit=False)
    else:
        form=UserCreate()
    return render(request,'add_user.html',{'form':form})
