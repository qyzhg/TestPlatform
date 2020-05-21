from django.shortcuts import render,HttpResponse,redirect,reverse
from Person.models import Person
# Create your views here.
from Pro_inspection import models


def index(request):
    '''
    视察首页
    :param request:
    :return:
    '''
    inspection_errors = models.InspectionErrors.objects.filter(is_del=False).order_by('-state')
    return render(request, 'pro_inspection/inspection_index.html',context=locals())


def start(request):
    '''

    :param request:
    :return:
    '''
    return redirect(reverse('pro_inspection:index'))


def state(request):
    '''
    状态修改
    :param request:
    :return:
    '''
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk = error_pk).first()
    if error.state:
        error.state = False
        error.save()
    else:
        error.state = True
        error.save()
    return redirect(reverse('pro_inspection:index'))


def pro_inspection_add(request):
    '''
    添加问题
    :param request:
    :return:
    '''
    if request.method == 'GET':
        all_person = Person.objects.filter(person_is_del=False)
        return render(request,'pro_inspection/inspection_add.html',context=locals())
    elif request.method == 'POST':
        error_name = request.POST.get('error')
        error_person = request.POST.get('person_pk')
        isgrave = request.POST.get('isgrave')#是否严重问题
        if isgrave == 'on':
            isgrave = True
        else:
            isgrave = False
        models.InspectionErrors.objects.create(error_name=error_name,person_id = error_person,is_severity=isgrave)
        return redirect(reverse('pro_inspection:index'))


def pro_inspection_del(request):
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk = error_pk).first()
    error.is_del = True
    error.save()
    return redirect(reverse('pro_inspection:index'))


def pro_inspection_isgrave(request):
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk = error_pk).first()
    if error.is_severity:
        error.is_severity = False
        error.save()
    else:
        error.is_severity = True
        error.save()
    return redirect(reverse('pro_inspection:index'))