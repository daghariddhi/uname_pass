from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import VerificationView

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_complete"),
    
    path('forgot_uname', views.forgot_uname, name="forgot_uname"),
    path('emailverificationmsg', views.email_ver_msg, name="email_ver_msg"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('uname_pass', views.uname_pass, name="uname_pass"),

]
