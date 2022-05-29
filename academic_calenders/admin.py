import imp
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Regulation)
admin.site.register(AcademicCalender)
admin.site.register(Graduation)
admin.site.register(Department)
admin.site.register(Batch)