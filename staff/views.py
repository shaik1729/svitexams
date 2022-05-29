from django.shortcuts import render
from django.http import HttpResponse
from .models import StaffDetails

# Create your views here.
def index(request):
    staffDetails = StaffDetails.objects.all().order_by('-department')
    return render(request,'staff.html',{'staffDetails' : staffDetails})
