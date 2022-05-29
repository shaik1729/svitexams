from django.shortcuts import render
from django.http import HttpResponse
from .models import Circular

# Create your views here.
def index(request):
    circulars = Circular.objects.all()
    return render(request,'index.html', {'circulars' : circulars})
