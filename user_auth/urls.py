from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('signup/', SignUpView.as_view(), name="signup"),
    
    path('authenticate_user/', views.authenticate_user,
name='authenticate_user'),
    path('user/', views.show_user, name='show_user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]