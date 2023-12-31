from django.urls import path
from django.urls import reverse_lazy
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
# Cliente 
    # Login and Logout
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/commons/password_change_form.html',
            success_url = '/accounts/login/'
        ),
        name='change_password'
    ),

# Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/commons/password_reset_form.html',
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/commons/password_reset_email.html',
             success_url= reverse_lazy('contas:password_reset_done'),
         ),
         name='senha_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/commons/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/commons/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/commons/password_reset_complete.html'
         ),
         name='password_reset_complete'),

# Cliente 
    path('new_user/', views.new_user, name='new_user'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_update/<int:pk>/', views.edit_profile, name='edit_profile'),
    path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('user_bio/<int:pk>/', views.edit_bio, name='edit_bio'),
    
]
