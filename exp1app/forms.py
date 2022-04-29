from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group


##問題を整理する
##プルダウンでユーザーに対してどのような権限を与えるのか設定できるようにしたい。
##今発生している問題はユーザーに対して与える権限がコントロールできていないこと
##具体的にはforms.pyではログインユーザーが共有できておらず、ログインユーザーが所属するグループのみを表示させることができない。
##グループユーザーが所属するグループには権限の種類がいくつかあり、そのうちいくつかを渡したい。
##つまり、ログインユーザーが所属しているグループさえわかれば、それをもとにプルダウンを作れる
##しかし、views.pyからforms.pyにユーザー情報をつなげられていない。
##
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='必須 有効なメールアドレスを入力してください。',
        label='Eメールアドレス',
    )
    permission = forms.ModelChoiceField(
        label="権限",
        queryset=Group.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','permission')
