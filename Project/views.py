from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
from Project import models
from Person import models as person_models


def start(request):
    return redirect(reverse('project:index'))


def index(request):
    all_projects = models.Project.objects.filter(project_is_del=False)
    return render(request,'project/project_list.html',context=locals())


def project_add(request):
    if request.method == 'GET':
        all_person = person_models.Person.objects.filter(person_is_del=False)
        return render(request,'project/project_add.html',context=locals())
    elif request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_persons = request.POST.getlist('persons')
        new_project = models.Project.objects.create(project_name=project_name)
        new_project.person_set.set(project_persons)
        return redirect(reverse('project:index'))


def project_del(request):
    project_pk = request.GET.get('pk')
    project = models.Project.objects.filter(pk = project_pk).first()
    project.project_is_del = True
    project.save()
    return redirect(reverse('project:index'))


def project_edit(request):
    if request.method == 'GET':
        project_pk = request.GET.get('pk')
        project = models.Project.objects.filter(pk = project_pk).first()
        all_person = person_models.Person.objects.filter(person_is_del=False)
        project_person = project.person_set.all()
        return render(request,'project/project_edit.html',context=locals())

    if request.method == 'POST':
        project_pk = request.POST.get('project_pk')
