from django.db import models

# Create your models here.

class InspectionErrors(models.Model):
    '''
    视察问题记录
    '''
    error_name = models.CharField(max_length=256)   #问题名
    state = models.BooleanField(default=True)       #状态
    is_severity = models.BooleanField(default=True) #是否严重
    person = models.ForeignKey('Person.Person',on_delete=models.CASCADE)   #操作人外键
    is_del = models.BooleanField(default=False) #逻辑删除