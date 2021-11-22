from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')

def library(request):
    return render(request, 'library.html')