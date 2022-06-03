from django.db import models
from datetime import datetime


# Create your models here.
class Circular(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    doc_url = models.URLField(max_length=1000)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
