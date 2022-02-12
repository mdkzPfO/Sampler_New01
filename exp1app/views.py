from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import SamplingModel,ReportModel,AnimalModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def TopPageView(request):
    return render(request,'Function/Top_Page.html',{})


def loginview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            return redirect('Top_Page')
        else:
            return redirect('login')
    return render(request,'registration/login.html')

def signupview(request):
    print(request.POST.get('username_data'))
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            print("わっしょい")
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています'})
    else:
        return render(request,'signup.html',{})
    return render(request,'signup.html',{})

class ReportPageClass(CreateView):
    template_name='Function/Report/Report_Page.html'
    model=ReportModel
    fields=('status','suggestion')
    success_url=reverse_lazy('Report_List')

@login_required
def ReportListView(request):
    object_list=ReportModel.objects.all()
    return render(request,'Function/Report/Report_List.html',{'object_list':object_list})

@login_required
def ReportCheckView(request):
    object=ReportModel.objects.get(pk=pk)
    return render(request,'Function/Report/Report_Check.html',{'object':object})

class SamplingPageClass(CreateView):
    template_name='Function/Sampling/Sampling_Page.html'
    model=SamplingModel
    fields=('title','animal','purpose','method','control_number','control_situation','experiment_number','experiment_situation')
    success_url=reverse_lazy('Sampling_List')

@login_required
def SamplingListView(request):
    object_list=SamplingModel.objects.all()
    return render(request,'Function/Sampling/Sampling_List.html',{'object_list':object_list})

@login_required
def SamplingCheckView(request,pk):
    object=SamplingModel.objects.get(pk=pk)
    return render(request,'Function/Sampling/Sampling_Check.html',{'object':object})

@login_required
def PreserveCheckView(request):
    return render(request,'Function/Preserve/Preserve_Check.html',{})

@login_required
def PreserveListView(request):
    return render(request,'Function/Preserve/Preserve_List.html',{})


class AnimalPageClass(CreateView):
    template_name='Function/Animal/Animal_Page.html'
    model=AnimalModel
    fields=('Animal','manager','wash','wash_frequency','feed','feed_frequency','temprature','location')
    success_url=reverse_lazy('Animal_List')

@login_required
def AnimalListView(request):
    object_list=AnimalModel.objects.all()
    print("テステス")
    print(object_list)
    return render(request,'Function/Animal/Animal_List.html',{'object_list':object_list})

@login_required
def AnimalCheckView(request,pk):
    object=AnimalModel.objects.get(pk=pk)
    return render(request,'Function/Animal/Animal_Check.html',{'object':object})
