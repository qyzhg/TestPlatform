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

class MakeData(models.Model):
    name = models.CharField(max_length=256) #模块名

class MakeData_cache(models.Model):
    ip = models.CharField(max_length=15)
    port = models.IntegerField(max_length=5)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    updata_time = models.DateTimeField(auto_now=True,verbose_name='updata_time')
    last_models = models.ForeignKey(MakeData,on_delete=models.CASCADE)