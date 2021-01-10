"""taskmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from task.views import register_view, add_task_view, FetchAllTasks, review_task_view

urlpatterns = [
    path('api/v1/auth/register', register_view, name='register'),
    path('api/v1/auth/login', TokenObtainPairView.as_view(), name='token'),
    path('api/v1/auth/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('api/v1/tasks/addTask', add_task_view, name='addTask'),
    path('api/v1/tasks/reviewTask', review_task_view, name='reviewTask'),
    path('api/v1/tasks/fetchAll', FetchAllTasks.as_view(), name='FetchTasks'),
]
