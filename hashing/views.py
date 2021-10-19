from django.shortcuts import render, redirect
from .forms import *
from .models import *
import hashlib
from django.http import JsonResponse
# Create your views here.

def homee(request):
    return render(request,'hashing/homee.html')

def home(request):
    if request.method == 'POST': # If the form has been submitted...
        filled_form = HashForm(request.POST) # A form bound to the POST data
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
        return redirect('hash',hash=text_hash)

    form = HashForm()
    return render(request, 'hashing/home.html',{'form': form})

def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    return render(request,'hashing/hash.html',{'hash':hash})

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash':hashlib.sha256(text.encode('utf-8')).hexdigest()})