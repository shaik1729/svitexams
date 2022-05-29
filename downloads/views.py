from django.shortcuts import render
from django.http import HttpResponse
from .models import Download

# Create your views here.
def index(request):
    svit_downloads = Download.objects.filter(category_id=1)
    jntua_downloads = Download.objects.filter(category_id=2)
    downloads = {"svit" : svit_downloads, "jntua" : jntua_downloads}
    return render(request,'downloads.html',{'downloads' : downloads})
