import imp
from time import time
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import ExamTimeTable

# Create your views here.
def index(request):
    svit_time_tables = ExamTimeTable.objects.filter(category_id=1)
    jntua_time_tables = ExamTimeTable.objects.filter(category_id=2)
    time_tables = {"svit" : svit_time_tables, "jntua" : jntua_time_tables}
    return render(request,'exam_time_tables.html',{'time_tables' : time_tables})
