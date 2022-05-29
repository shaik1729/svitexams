from django.db import models
from pkg_resources import require

# Create your models here.

class FacultyDept(models.Model):
    dept = models.CharField(max_length=30)

    def __str__(self):
        return self.dept

class StaffDetails(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(FacultyDept, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=15)
    main_id = models.EmailField(max_length=254,unique=True)
    profile = models.URLField(max_length=200, default='', blank=True)

    def __str__(self):
        return self.name+" "+self.department.dept

