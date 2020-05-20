from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=128)
    project_is_del = models.BooleanField(default=False)