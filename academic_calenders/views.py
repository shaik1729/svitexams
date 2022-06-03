from django.shortcuts import render
from django.http import HttpResponse
from .models import AcademicCalender

# Create your views here.
def index(request):
    calenders = AcademicCalender.objects.all().order_by('-created_date')
    return render(request,'academic_calenders.html',{'calenders' : calenders})
