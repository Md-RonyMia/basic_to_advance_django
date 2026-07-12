from django.shortcuts import render,redirect
from .forms import PostForm
from . import models

def PostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            form.save()  # If AuthorForm is a ModelForm
    else:
        form = PostForm()

    return render(request, 'add_category.html', {'form': form})



def edit_post(request,id):
    post = models.Post.objects.get(pk=id)
    post_form=PostForm(instance=post)
    if request.method == 'POST':
        post_form=form.PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            form.save()  # If AuthorForm is a ModelForm
    else:
        form = PostForm()

    return render(request, 'add_category.html', {'form': post_form})



def delete_post(request,id):
    post = models.Post.objects.get(pk=id).delete()
    return redirect('home')
