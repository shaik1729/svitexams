"""svitexams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('circulars.urls')),
    path('exam_time_tables',include('exam_time_tables.urls')),
    path('notifications',include('notifications.urls')),
    path('academic_calenders',include('academic_calenders.urls')),
    path('syllabus',include('syllabus.urls')),
    path('downloads',include('downloads.urls')),
    path('staff',include('staff.urls')),
    path('about',include('about.urls')),
    path('results',include('results.urls')),
    path('students_data',include('students_data.urls')),

]
