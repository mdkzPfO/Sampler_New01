from django.urls import path,include
from . import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'
urlpatterns = [
    path('activation_request/', auth_views.activation_request, name='activation_request'),
    path('activate/<uidb64>/<token>/', auth_views.activate, name='activate'),
    path('signup/',auth_views.signup,name='default_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/reset-password-done.html'),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/change-password-done.html'), name='password_change_done'), #追加
    ]
