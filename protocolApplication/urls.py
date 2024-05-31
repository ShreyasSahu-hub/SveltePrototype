"""MasterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path, include
#
# from protocolApplication.views import helloworld,AddTask,UpdateTask,RetrieveTask,DeleteTaskDetails, SignUp, Login
#
# urlpatterns = [
# #     path('', helloworld),
#     path("signup/", SignUp, name='signup'),
#     path("login/", Login, name="login"),
#     path('TaskInsert/',AddTask),
#     path('TaskUpdate/',UpdateTask),
#     path('RetrieveTaskDetails/',RetrieveTask),
#     path('DeleteTaskDetail/',DeleteTaskDetails)
# ]

from django.urls import path
# from films.views import FilmListAPIView, FilmDetailAPIView
#from protocolApplication.views import FilmViewSet
from protocolApplication.views import TaskViewSet, SignUp, Login,AddTask
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
urlpatterns = router.urls

urlpatterns +=[path('TaskInsert/',AddTask)]