"""ssm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from ssm_app.views import homepage, show_music_view, MyPasswordChangeView, show_blog_view, \
    register_view, login_view, logout_view, subscribe_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('music/', show_music_view, name='music'),
    path('blog/', show_blog_view, name='blog'),
    # CHANGE PASSWORD
    path('password-change/', MyPasswordChangeView.as_view(), name='password_change'),
    # SUBSCRIPTION
    path('subscription/', subscribe_view, name='subscribe'),
    # REGISTRATION
    path('register/', register_view, name='register'),
    # LOGIN
    path('login/', login_view, name='login'),
    # LOGOUT
    path('logout/', logout_view, name='logout')
]

urlpatterns += staticfiles_urlpatterns()
