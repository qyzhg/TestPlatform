from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
def start(request):
    return redirect(reverse('index:index'))


def index(request):
    return render(request,'index/index.html')