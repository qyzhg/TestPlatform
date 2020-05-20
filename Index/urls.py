#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   urls.py
 
@Time    :   2020/5/20 10:23 上午
'''


from django.urls import path

from Index import views



urlpatterns = [
    path('',views.start,name='start'),
    path('index/',views.index,name='index'),
]