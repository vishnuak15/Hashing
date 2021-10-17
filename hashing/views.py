from django.shortcuts import render
from .forms import *
# Create your views here.

def home(request):
    form_class = HashForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST': # If the form has been submitted...
        form = HashForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            print(form.cleaned_data['text'])
    return render(request, 'hashing/home.html',{'form': form})