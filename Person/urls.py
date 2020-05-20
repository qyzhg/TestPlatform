#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   urls.py
 
@Time    :   2020/5/20 10:23 上午
'''


from django.urls import path

from Person import views


urlpatterns = [
    path('',views.start,name='start'),
    path('index/',views.index,name='index'),                    #首页
    path('person_add/',views.person_add,name='person_add'),     #添加页
    path('person_del/',views.person_del,name='person_del'),     #删除功能
    path('person_edit/',views.person_edit,name='person_edit'),     #修改功能
]