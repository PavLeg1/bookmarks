from django.urls import path, include 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Предыдущий url входа
    # path('login/', views.user_login, name='login'),

    # # url входа и выхода
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    

    # # url смены пароля
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # url сброса пароля
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Подключаем все закомментированные url сверху
    path('', include('django.contrib.auth.urls')),
    
    path('', views.dashboard, name='dashboard'),


]
