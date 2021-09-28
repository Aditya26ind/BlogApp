
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import changePassword, index,signuppage,loginuser,logoutuser
urlpatterns = [
     path('',index),
     path('signup/',signuppage,name='signup'),
     path('login/',loginuser,name='login'),
     path('logout/',logoutuser,name='login'),
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),
     path('reset_password/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='reset_passwordtoken.html'),name='password_reset_confirm'),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='password_reset_complete')

]
