from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include("user_auth.urls")),
    path("signup/", include("user_auth.urls")),
    path("signup/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="user.html"), name="home"),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_auth/templates/logout.html'), name='logout'),
]
