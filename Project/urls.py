#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   urls.py
 
@Time    :   2020/5/20 10:42 上午
'''


from django.urls import path

from Project import views


urlpatterns = [
    path('',views.start,name='start'),
    path('index/',views.index,name='index'),
    path('project_add/',views.project_add,name='project_add'),
    path('project_del/',views.project_del,name='project_del'),
    path('project_edit/',views.project_edit,name='project_edit'),
]