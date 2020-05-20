from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
from Person import models
from Project import models as project_models


def start(request):
    '''
    没写路径的重定向到index
    :param request:
    :return:
    '''
    return redirect(reverse('person:index'))


def index(request):
    '''
    首页
    :param request:
    :return:
    '''
    persons = models.Person.objects.filter(person_is_del=False)
    return render(request,'person/person_list.html',context=locals())


def person_add(request):
    '''
    添加人员
    :param request:
    :return:
    '''
    if request.method == 'GET':
        projects = project_models.Project.objects.filter(project_is_del=False)
        return render(request,'person/person_add.html',context=locals())
    elif request.method == 'POST':
        # 接收表单参数
        person_name = request.POST.get('person_name')           #人员姓名
        project_pk_list = request.POST.getlist('project')       #项目主键(列表）
        #写数据入库
        new_person = models.Person.objects.create(person_name=person_name)
        new_person.person_project.set(project_pk_list)
        return redirect(reverse('person:index'))


def person_del(request):
    '''
    删除人员
    :param request:
    :return:
    '''
    person_pk = request.GET.get('pk')
    person = models.Person
    del_person = person.objects.filter(pk = person_pk).first()
    del_person.person_is_del = True
    del_person.save()
    return redirect(reverse('person:index'))


def person_edit(request):
    '''
    修改人员
    :param request:
    :return:
    '''
    if request.method == 'GET':
        person_pk = request.GET.get('pk')
        person_name = models.Person.objects.filter(pk = person_pk).first().person_name
        person_project = models.Person.objects.filter(pk = person_pk).first().person_project.all()
        all_projects = project_models.Project.objects.filter(project_is_del=False)
        return render(request,'person/person_edit.html',context=locals())
    elif request.method == 'POST':
        #接收数据
        person_pk = request.POST.get('person_pk')
        person_name = request.POST.get('person_name')
        person_projects = request.POST.getlist('projects')
        #更改数据库
        person = models.Person.objects.filter(pk = person_pk).first()
        person.person_name = person_name
        person.person_project.set(person_projects)
        person.save()
        return redirect(reverse('person:index'))