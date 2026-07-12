from django.shortcuts import render
from .forms import CategoryForm

def CategoryView(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            form.save()  # If AuthorForm is a ModelForm
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})