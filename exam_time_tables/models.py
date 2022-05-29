from unicodedata import category
from django.db import models

# Create your models here.
class CollegeCategory(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category

class ExamTimeTable(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    doc_url = models.URLField(max_length=1000)
    category = models.ForeignKey(CollegeCategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title
