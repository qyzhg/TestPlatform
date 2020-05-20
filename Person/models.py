from django.db import models

# Create your models here.

class Person(models.Model):
    person_name = models.CharField(max_length=16)           #人员
    person_is_del = models.BooleanField(default=False)      #逻辑删除
    person_project = models.ManyToManyField('Project.Project')  #多对对关系，关联项目表