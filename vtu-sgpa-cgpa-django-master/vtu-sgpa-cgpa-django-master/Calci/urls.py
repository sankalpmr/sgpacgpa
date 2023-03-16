"""Calci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Calci import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mypage),
    path('cgpa/', views.cgpa),
    path('about/', views.about),
    path('sem/', views.sems),
    path('sem/sem1/', views.sem1),
    path('sem/sem2/', views.sem2),
    path('sem/sem3/', views.sem3),
    path('sem/sem4/', views.sem4),
    path('sem/sem5/', views.sem5),
    path('sem/sem6/', views.sem6),
    path('sem/sem7/', views.sem7),
    path('sem/sem8/', views.sem8),
]

