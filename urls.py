from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.user_registration, name='registration'),
    path('change_password/', views.change_password, name='change_password'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),

    path(
        'reset_password/', 
        auth_views.PasswordResetView.as_view(template_name='authenticate/password_reset.html'), 
        name='reset_password'
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset_sent.html'), 
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='authenticate/password_reset_form.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/password_reset_done.html'),
        name='password_reset_complete'
    ),
]
