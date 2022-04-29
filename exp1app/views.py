from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView
from .models import SamplingModel,ReportModel,AnimalModel,Original_GroupModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views import generic
from django.views.generic import ListView
#ManagedUser creation
from django.utils.http import (
    urlsafe_base64_encode,url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

###############################################################################アカウント作成関連-------------------------------ここから-------------------------------------------------------
##管理者によるユーザー追加---------------------ここから---------------------------
##詳細：参照するファイルをexp1appの中のファイルにしている。ほとんどaccountsアプリと同じ。元はdjangoに組み込まれているauthの認証機能だが、自分のフォームに合わせる為に、一部を変更している。
##signup(登録)→activation_request(メールにアクティブ化を要求)→activate(メールのリンクからアクティブ化を実施)
###サインアップ登録画面-----ここから
###詳細：ほとんどはaccountsアプリで使用するsignupと同じだが、ユーザーのgroupsに管理者と同じグループを発行している。
def signup(request):
    user=request.user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            machida=request.POST.get('permission')
            machida=int(machida)
            if machida==50:
                permission="User_Permission"
            elif machida==51:
                permission="Domain_Permission"
            elif machida==52:
                permission="OnlyView_Permission"
            test=Group.objects.get(name=permission)
            test.user_set.add(user)
            related_group=Original_GroupModel.objects.get(slave_user=request.user)
            print("ぽいぽい")
            print(related_group)
            print("ほいほい")
            sample = Original_GroupModel(origin_group=related_group.origin_group, slave_user=user)
            sample.save()
            current_site = get_current_site(request)
            subject = 'アクティベートする必要があります'
            message = render_to_string('Function/User_Creation/registration/email_body.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('exp1app:activation_request')
    else:
        form=SignUpForm()
    return render(request, 'Function/User_Creation/signup.html', {'form': form})
###サインアップ登録画面----ここまで


###サインアップ後のアクティブ化----ここから
def activation_request(request):
    return render(request, 'Function/User_Creation/registration/activation_request.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('accounts:login')
    else:
        return render(request, 'registration/activated.html')
###サインアップ後のアクティブ化--ここまで
##管理者によるユーザー追加---------ここまで--------------------------------------


##グループ作成ページ
#グループ名を作成し、管理者を強制的にそのグループに所属させる
#ここではグループモデルに紐づけて、所属させていたが新しくmanage-accountモデルを作る
class Group_Create(CreateView):
    template_name='Function/Resistration/Group_Create.html'
    model=Original_GroupModel
    model2=User
    fields=['origin_group']
    success_url=reverse_lazy('exp1app:Top_Page')
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        #この時点でグループ名は固定されたはず
        ##SQLなら動くかどうか調査予定
        self.object = form.save()
        my_group = Group.objects.get(name="Domain_Permission")
        my_group.user_set.add(self.request.user)
        return super().form_valid(form)

###ユーザーを管理者によって作成する為のリスト画面----ここから----------------------
#これまでのやり方ではuser情報のGroupsを更新しようとしていたが、
#多対多構成の場合は情報の更新ができないという仕様があり、反映されなかった。
#そこでユーザーを作成した場合には、メールとパスワードだけはuserテーブルと紐づけて、
#ドメイン権限・●●権限等の形で権限を分けてアカウントを発行す仕組みをとる
#ちなみにここで作成された新しいユーザー情報はユーザー+グループテーブルに記載される

class UserCreationList(ListView):
    template_name="Function/User_Creation/UserCreationList.html"
    model=Original_GroupModel
    paginate_by=2
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "auth.view_user" in permission:
            login_user=self.request.user
            login_group=Original_GroupModel.objects.filter(slave_user=login_user)
            #リスト0で動くか確認
            for i in login_group:
                login_group_name=i.origin_group
            Same_Group_Users=Original_GroupModel.objects.filter(origin_group=login_group_name)
            Same_Group_UsersList=list()
            for i in Same_Group_Users:
                Same_Group_UsersList.append(i.slave_user)
            object_list=list()
            for i in Same_Group_UsersList:
                Same_Groups_Users_Object = User.objects.filter(username=i)
                if Same_Groups_Users_Object.first() is None:
                    continue
                else:
                    for k in Same_Groups_Users_Object:
                        object_list.append(k)
            context = {"object_list": object_list}
            return render(request, 'Function/User_Creation/UserCreationList.html', context)
        return redirect('exp1app:Top_Page')
    def get_queryset(self):
        ##後で修正

        if self.request.user.id is None:
            print("ほいほい")
            logined_group=None
        else:
            print("ちょいちょい")
            logined_group=self.request.user.groups
            print(logined_group)
        groups_box=self.request.user.groups.all()
        Belong_GroupName= Original_GroupModel.objects.get(slave_user=self.request.user)
        object_list=Original_GroupModel.objects.filter(origin_group=Belong_GroupName.origin_group)
        slave_user_list=list()
        for i in object_list:
            slave_user_list.append(i.slave_user)
        object_list=slave_user_list
        print(object_list)
        q_word = self.request.GET.get('query')
        if q_word:
            object_list = User.objects.filter(
                Q(title__icontains=q_word))
        print(object_list)
        return object_list
###ユーザーを管理者によって作成するためのリスト画面---ここまで-------------------

###ユーザー情報更新用画面
class UserCreationList_Update(UpdateView):
    template_name = "Function/User_Creation/UserCreationList_Update.html"
    fields =('username','email')
    model=User
    def get_success_url(self):
        return reverse('exp1app:UserCreationList_Detail', kwargs={'pk': self.object.pk})
    def get_form(self):
        form = super(UserCreationList_Update, self).get_form()
        form.fields['username'].label='ユーザー名'
        form.fields['email'].label="メールアドレス"
        return form

class UserCreationList_Delete(DeleteView):
    model = User
    context_object_name = "UserModel"
    template_name="Function/User_Creation/UserCreationList_Delete.html"
    success_url = reverse_lazy("exp1app:User_List")

###ユーザー情報の詳細を確認可能な画面
class UserCreationList_Detail(DetailView):
    model=User
    context_object_name = "UserModel"
    template_name="Function/User_Creation/UserCreationList_Detail.html"
###############################################アカウント作成関連ここまで--------------------------------------------------------------------------------


######################################################Topページへ飛ばす-----ここから----------------------------------------------------------------------
def TopPageView(request):
    return render(request,'Function/Top_Page.html',{})
######################################################Topページへ飛ばす----ここまで-----------------------------------------------------------------------


#ログインしたユーザーに合わせて表示させる画面を変えたい
#その為にはログインユーザーの情報を取得する必要がある
#現状はなぜか{{user}}でログインユーザーの情報を取得できている

class SamplingList(ListView):
    template_name = 'Function/Sampling/SamplingList.html'
    model=SamplingModel
    paginate_by=2
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.view_samplingmodel" in permission:
            login_user=self.request.user
            login_group=Original_GroupModel.objects.filter(slave_user=login_user)
            #リスト0で動くか確認
            for i in login_group:
                login_group_name=i.origin_group
            Same_Group_Users=Original_GroupModel.objects.filter(origin_group=login_group_name)
            Same_Group_UsersList=list()
            for i in Same_Group_Users:
                Same_Group_UsersList.append(i.slave_user)
            object_list=list()
            for i in Same_Group_UsersList:
                Same_Groups_Users_Object = SamplingModel.objects.filter(user=i)
                if Same_Groups_Users_Object.first() is None:
                    continue
                else:
                    for k in Same_Groups_Users_Object:
                        object_list.append(k)
            context = {"object_list": object_list}
            return render(request, 'Function/Sampling/SamplingList.html', context)
        return redirect('exp1app:Top_Page')
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
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.add_samplingmodel" in permission:
            return render(request, 'Function/Sampling/SamplingList_Create.html')
        return redirect('exp1app:Top_Page')

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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.change_samplingmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.delete_samplingmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')


class SamplingList_Detail(DetailView):
    model=SamplingModel
    context_object_name = "SamplingModel"
    template_name="Function/Sampling/SamplingList_Detail.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.view_samplingmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')


class AnimalList(ListView):
    template_name = 'Function/Animal/AnimalList.html'
    model=AnimalModel
    paginate_by=2
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.view_animalmodel" in permission:
            login_user=self.request.user
            login_group=Original_GroupModel.objects.filter(slave_user=login_user)
            #リスト0で動くか確認
            for i in login_group:
                login_group_name=i.origin_group
            Same_Group_Users=Original_GroupModel.objects.filter(origin_group=login_group_name)
            Same_Group_UsersList=list()
            for i in Same_Group_Users:
                Same_Group_UsersList.append(i.slave_user)
            object_list=list()
            for i in Same_Group_UsersList:
                Same_Groups_Users_Object = AnimalModel.objects.filter(user=i)
                if Same_Groups_Users_Object.first() is None:
                    continue
                else:
                    for k in Same_Groups_Users_Object:
                        object_list.append(k)
            context = {"object_list": object_list}
            return render(request, 'Function/Animal/AnimalList.html', context)
        return redirect('exp1app:Top_Page')
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
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.add_animalmodel" in permission:
            return render(request, 'Function/Animal/AnimalList_Create.html')
        return redirect('exp1app:Top_Page')

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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.change_animalmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')

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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.delete_animalmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
class AnimalList_Detail(DetailView):
    model=AnimalModel
    context_object_name = "AnimalModel"
    template_name="Function/Animal/AnimalList_Detail.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.view_animalmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
class ReportList(ListView):
    template_name = 'Function/Report/ReportList.html'
    model=ReportModel
    paginate_by=2
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.view_reportmodel" in permission:
            login_user=self.request.user
            login_group=Original_GroupModel.objects.filter(slave_user=login_user)
            #リスト0で動くか確認
            for i in login_group:
                login_group_name=i.origin_group
            Same_Group_Users=Original_GroupModel.objects.filter(origin_group=login_group_name)
            Same_Group_UsersList=list()
            for i in Same_Group_Users:
                Same_Group_UsersList.append(i.slave_user)
            object_list=list()
            for i in Same_Group_UsersList:
                Same_Groups_Users_Object = ReportModel.objects.filter(user=i)
                if Same_Groups_Users_Object.first() is None:
                    continue
                else:
                    for k in Same_Groups_Users_Object:
                        object_list.append(k)
            context = {"object_list": object_list}
            return render(request, 'Function/Report/ReportList.html', context)
        return redirect('exp1app:Top_Page')
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
    def get(self, request):
        #利用者の権限を確認する
        permission=self.request.user.get_group_permissions()
        #もし閲覧権限があれば...
        if "exp1app.add_reportmodel" in permission:
            return render(request, 'Function/Report/ReportList_Create.html')
        return redirect('exp1app:Top_Page')

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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.change_reportmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
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
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.delete_reportmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
class ReportList_Detail(DetailView):
    model=ReportModel
    context_object_name = "ReportModel"
    template_name="Function/Report/ReportList_Detail.html"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        permission=self.request.user.get_group_permissions()
        if "exp1app.view_reportmodel" in permission:
            return super().get(request, *args, **kwargs)
        return redirect('exp1app:Top_Page')
