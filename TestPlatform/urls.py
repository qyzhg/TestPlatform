"""TestPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('Index.urls','Index'),namespace='index')),
    path('person/', include(('Person.urls','Person'),namespace='person')),      #人员管理
    path('project/', include(('Project.urls','Project'),namespace='project')),  #项目管理
    path('pro_inspection/', include(('Pro_inspection.urls','Pro_inspection'),namespace='pro_inspection')),  #项目—视察管理
]
