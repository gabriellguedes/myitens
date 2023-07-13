from django.urls import path
from django.urls import reverse_lazy
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
# Cliente 
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
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
    path('new_client/', views.new_user, name='new_user'),
    path('new_user/', views.user_add, name='cliente_add'),
    path('novo_cliente/', views.cliente_add, name='new_cliente_add'),
    path('user_list/', views.user_list, name='cliente_list'),
    path('use_profile/<int:pk>/', views.user_profile, name='user_profile'),
    path('user_detail/<int:pk>/', views.user_detail, name='cliente_detail'),
    path('user_update/<int:pk>/', views.user_update, name='cliente_update'),
    path('user_update_for_adm/<int:pk>/', views.user_update_for_adm, name='user_update_for_adm'),
    path('user_delete/<int:pk>/', views.user_delete, name='cliente_delete'),

   
    
]