from django.shortcuts import render
from django.http import HttpResponse
from .models import Syllabus

# Create your views here.
def index(request):
    syllabus = Syllabus.objects.all().order_by('-created_date')
    return render(request,'syllabus.html',{'syllabus' : syllabus})
