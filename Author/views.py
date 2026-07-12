from django.shortcuts import render
from .forms import AuthorForm

def authorview(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            form.save()  # If AuthorForm is a ModelForm
    else:
        form = AuthorForm()

    return render(request, 'add_author.html', {'form': form})