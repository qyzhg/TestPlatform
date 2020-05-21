#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   urls.py
 
@Time    :   2020/5/21 9:02 上午
'''
from django.urls import path

from Pro_inspection import views

urlpatterns = [
    path('', views.start, name='start'),
    path('index/', views.index, name='index'),
    path('state/', views.state, name='state'),
    path('pro_inspection_add/', views.pro_inspection_add, name='pro_inspection_add'),
    path('pro_inspection_del/', views.pro_inspection_del, name='pro_inspection_del'),
    path('pro_inspection_isgrave/', views.pro_inspection_isgrave, name='pro_inspection_isgrave'),
    path('pro_inspection_recycle/', views.pro_inspection_recycle, name='pro_inspection_recycle'),  # 回收站
    path('pro_inspection_restore/', views.pro_inspection_restore, name='pro_inspection_restore'),  # 还原
]
