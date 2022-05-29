from django.db import models
from exam_time_tables.models import CollegeCategory
# Create your models here.

class Download(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    doc_url = models.URLField(max_length=1000)
    category = models.ForeignKey(CollegeCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title
