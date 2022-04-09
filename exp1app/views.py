from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView
from .models import SamplingModel,ReportModel,AnimalModel,UseChildrenModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

from django.views import generic
from django.views.generic import ListView

def TopPageView(request):
    return render(request,'Function/Top_Page.html',{})


class UserChildrenCreationView(CreateView):
    template_name='Function/Resistration/Children_Creation.html'
    model=UseChildrenModel
    fields=('Children_Name','Children_Email')
    success_url=reverse_lazy('exp1app:Top_Page')
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.user=self.request.user
        qryset.save()
        return  redirect('exp1app:Top_Page')


#ログインしたユーザーに合わせて表示させる画面を変えたい
#その為にはログインユーザーの情報を取得する必要がある
#現状はなぜか{{user}}でログインユーザーの情報を取得できている様子


class SamplingList(ListView):
    template_name = 'Function/Sampling/SamplingList.html'
    model=SamplingModel
    paginate_by=2
    def get_queryset(self):
        if self.request.user.id is None:
            logined_user=None
        else:
            logined_user=self.request.user
        object_list = SamplingModel.objects.filter( user = logined_user )
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = SamplingModel.objects.filter(
                Q(title__icontains=q_word))
        return object_list

class SamplingList_Create(CreateView):
    template_name='Function/Sampling/SamplingList_Create.html'
    model=SamplingModel
    fields=['animal','title','purpose','method','control_number','control_situation','experiment_number','experiment_situation']
    success_url=reverse_lazy('exp1app:Sampling_List')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.user=self.request.user
        qryset.save()
        return  redirect('exp1app:Sampling_List')

#更新時に値が格納されていないものがあっても許容する
#値が格納されていなければ、既に設定されているデータを変更しない
#既存のデータを上に出したほうが見栄えがよさそう
class SamplingList_Update(UpdateView):
    template_name = "Function/Sampling/SamplingList_Update.html"
    fields =('title','animal','purpose','method','control_number','control_situation','experiment_number','experiment_situation')
    model=SamplingModel
    def get_success_url(self):
        return reverse('exp1app:SamplingList_Detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(SamplingList_Update, self).get_form()
        form.fields['title'].label='サンプリング名'
        form.fields['animal'].label='サンプリング対象'
        form.fields['purpose'].label='サンプリング目的'
        form.fields['method'].label='サンプリング方法'
        form.fields['control_number'].label='コントロール数'
        form.fields['control_situation'].label='コントロール条件'
        form.fields['experiment_number'].label='実験群'
        form.fields['experiment_situation'].label='実験条件'
        return form

class SamplingList_Delete(DeleteView):
    model = SamplingModel
    context_object_name = "SamplingModel"
    template_name="Function/Sampling/SamplingList_Delete.html"
    success_url = reverse_lazy("exp1app:Sampling_List")

class SamplingList_Detail(DetailView):
    model=SamplingModel
    context_object_name = "SamplingModel"
    template_name="Function/Sampling/SamplingList_Detail.html"


class AnimalList(ListView):
    template_name = 'Function/Animal/AnimalList.html'
    model=AnimalModel
    paginate_by=2
    def get_queryset(self):
        if self.request.user.id is None:
            logined_user=None
        else:
            logined_user=self.request.user
        object_list =AnimalModel.objects.filter( user = logined_user )
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = AnimalModel.objects.filter(
                Q(title__icontains=q_word))
        return object_list

class AnimalList_Create(CreateView):
    template_name='Function/Animal/AnimalList_Create.html'
    model=AnimalModel
    fields=('animal','animal_purpose','manager','wash','wash_frequency','feed','feed_frequency','temprature','location')
    success_url=reverse_lazy('exp1app:Animal_List')
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.user=self.request.user
        qryset.save()
        return  redirect('exp1app:Animal_List')

class AnimalList_Update(UpdateView):
    template_name = "Function/Animal/AnimalList_Update.html"

    fields=('animal','animal_purpose','manager','wash','wash_frequency','feed','feed_frequency','temprature','location')
    model=AnimalModel
    def get_success_url(self):
        return reverse('exp1app:AnimalList_Detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(AnimalList_Update, self).get_form()
        form.fields['animal'].label='生物名'
        form.fields['animal_purpose'].label='飼育目的'
        form.fields['manager'].label='管理責任者'
        form.fields['wash'].label='洗浄方法'
        form.fields['wash_frequency'].label='洗浄頻度'
        form.fields['feed'].label='餌'
        form.fields['feed_frequency'].label='餌頻度'
        form.fields['temprature'].label='適温'
        form.fields['location'].label='場所'
        return form
class AnimalList_Delete(DeleteView):
    model = AnimalModel
    context_object_name = "AnimalModel"
    template_name="Function/Animal/AnimalList_Delete.html"
    success_url = reverse_lazy("exp1app:Animal_List")

class AnimalList_Detail(DetailView):
    model=AnimalModel
    context_object_name = "AnimalModel"
    template_name="Function/Animal/AnimalList_Detail.html"



class ReportList(ListView):
    template_name = 'Function/Report/ReportList.html'
    model=ReportModel
    paginate_by=2
    def get_queryset(self):
        if self.request.user.id is None:
            logined_user=None
        else:
            logined_user=self.request.user
        object_list = ReportModel.objects.filter( user = logined_user )
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = ReportModel.objects.filter(
                Q(title__icontains=q_word))
        return object_list

class ReportList_Create(CreateView):
    template_name='Function/Report/ReportList_Create.html'
    model=ReportModel
    fields=('status','suggestion')
    success_url=reverse_lazy('exp1app:Report_List')
    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.user=self.request.user
        qryset.save()
        return  redirect('exp1app:Report_List')



#更新時に値が格納されていないものがあっても許容する
#値が格納されていなければ、既に設定されているデータを変更しない
#既存のデータを上に出したほうが見栄えがよさそう
class ReportList_Update(UpdateView):
    template_name = "Function/Report/ReportList_Update.html"
    fields=('status','suggestion')
    model=ReportModel
    def get_success_url(self):
        return reverse('exp1app:ReportList_Detail', kwargs={'pk': self.object.pk})

    def get_form(self):
        form = super(ReportList_Update, self).get_form()
        form.fields['status'].label='ステータス'
        form.fields['suggestion'].label='報告'
        return form

class ReportList_Delete(DeleteView):
    model = ReportModel
    context_object_name = "ReportModel"
    template_name="Function/Report/ReportList_Delete.html"
    success_url = reverse_lazy("exp1app:Report_List")

class ReportList_Detail(DetailView):
    model=ReportModel
    context_object_name = "ReportModel"
    template_name="Function/Report/ReportList_Detail.html"
