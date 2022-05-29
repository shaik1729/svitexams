from datetime import datetime
from statistics import mode
from django.db import models
from academic_calenders.models import Regulation
from academic_calenders.models import Graduation
from academic_calenders.models import Batch


# Create your models here.


class Syllabus(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    doc_url = models.URLField(max_length=1000)
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE)
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
