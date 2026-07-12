from django.shortcuts import render
from Post.models import Post

# Create your views here.

def Home(request):
    all=Post.objects.all()
    return render(request,'index.html',{'all_post':all})


