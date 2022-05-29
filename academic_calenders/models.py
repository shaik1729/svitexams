from datetime import datetime
from django.db import models

# Create your models here.
class Graduation(models.Model):
    graduation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.graduation


class Batch(models.Model):
    batch = models.CharField(max_length=10)
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)

    def __str__(self):
        return self.batch+" "+self.graduation.graduation

class Department(models.Model):
    department = models.CharField(max_length=50)
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)


    def __str__(self):
        return self.department+" "+self.graduation.graduation+" "+self.batch.batch

class Regulation(models.Model):
    regulation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.regulation

class AcademicCalender(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    doc_url = models.URLField(max_length=1000)
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
