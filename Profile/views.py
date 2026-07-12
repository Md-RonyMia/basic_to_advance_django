from django.shortcuts import render
from .forms import ProfileForm

def ProfileView(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)   # Better than request.POST
            # form.save()  # If AuthorForm is a ModelForm
    else:
        form = ProfileForm()

    return render(request, 'add_profile.html', {'form': form})