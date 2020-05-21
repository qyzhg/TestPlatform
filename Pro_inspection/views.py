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
    '''
    删除问题
    :param request:
    :return:
    '''
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk = error_pk).first()
    error.is_del = True
    error.save()
    return redirect(reverse('pro_inspection:index'))


def pro_inspection_isgrave(request):
    '''
    移动问题
    :param request:
    :return:
    '''
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk = error_pk).first()
    if error.is_severity:
        error.is_severity = False
        error.save()
    else:
        error.is_severity = True
        error.save()
    return redirect(reverse('pro_inspection:index'))


def pro_inspection_recycle(request):
    '''
    回收站
    :param request:
    :return:
    '''
    if request.method == 'GET':
        del_error = models.InspectionErrors.objects.filter(is_del=True)
        return render(request,'pro_inspection/inspection_recycle.html',context=locals())


def pro_inspection_restore(request):
    '''
    还原回收站
    :param request:
    :return:
    '''
    error_pk = request.GET.get('pk')
    error = models.InspectionErrors.objects.filter(pk=error_pk).first()
    error.is_del = False
    error.save()
    return redirect(reverse('pro_inspection:pro_inspection_recycle'))


def performance_test(request):
    '''
    性能测试入口（工具选择入口）
    :param request:
    :return:
    '''
    return render(request,'pro_inspection/performance_test/performance_test.html')


def make_data(request):
    '''
    灌数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        ip = models.MakeData_cache.objects.all().order_by('-updata_time').first().ip
        port = models.MakeData_cache.objects.all().order_by('-updata_time').first().port
        tool_models = models.MakeData.objects.all()    #所有模块
        last_models = models.MakeData_cache.objects.all().order_by('-updata_time').first().last_models #最后使用模块
        last_username = models.MakeData_cache.objects.all().order_by('-updata_time').first().username
        last_pwd = models.MakeData_cache.objects.all().order_by('-updata_time').first().password
        return render(request,'pro_inspection/performance_test/make_data.html',context=locals())
    elif request.method == 'POST':
        ip = request.POST.get('server_ip')          #目标ip
        port = request.POST.get('server_port')      #目标端口
        model_pk = request.POST.get('mo_pk')        #选择的主键
        data_size = request.POST.get('data_size')   #数据量
        concurrence = request.POST.get('concurrence')#并发量
        username = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        #信息记录到缓存表
        new_cache = models.MakeData_cache
        new_cache.objects.create(
                                ip=ip,
                                port=port,
                                username=username,
                                password=pwd,
                                last_models_id=model_pk
                                )
        return redirect(reverse('pro_inspection:make_data'))