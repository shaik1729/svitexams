from sre_constants import BRANCH
from django.db import models
from pkg_resources import require
from academic_calenders.models import Department
from academic_calenders.models import Batch
from academic_calenders.models import Graduation



# Create your models here.
class StudentsData(models.Model):
    graduation = models.ForeignKey(Graduation, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_url = models.URLField(max_length=1000)

    def __str__(self):
        title_data = []
        title_data.append(self.graduation.graduation)
        title_data.append(self.batch.batch)
        title_data.append(self.department.department)
        title = " ".join(title_data)

        return title
