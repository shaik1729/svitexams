from django.shortcuts import render
from django.http import HttpResponse
from .models import Notification

# Create your views here.
def index(request):
    svit_notifications = Notification.objects.filter(category_id=1)
    jntua_notifications = Notification.objects.filter(category_id=2)
    notifications = {"svit" : svit_notifications, "jntua" : jntua_notifications}
    return render(request,'notifications.html',{'notifications' : notifications})
