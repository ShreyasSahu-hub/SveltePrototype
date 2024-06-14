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
from django.contrib import admin
from django.urls import path, include
#from protocolApplication.views import helloworld,AddTask,UpdateTask,RetrieveTask,DeleteTaskDetails, SignUp, Login
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static
from protocolApplication.views import SignUp, Login, AddTask, FetchTask, UpdateTask, DeleteTask, CalorieTracker, CalorieDetailRetrieved, print_test_results

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', lambda request: HttpResponse("health check")),
    path("login/", Login, name="login"),
    path("", Login, name="login"),
    path("signup/", SignUp, name='signup'),
    path('TaskInsert/',AddTask),
    path('TaskFetched/',FetchTask),
    path('TaskUpdate/', UpdateTask),
    path('TaskDelete/', DeleteTask),
    path('CalorieTracker/',CalorieTracker),
    path('RetrieveCalorieDetails/',CalorieDetailRetrieved),
    path('test_results/', print_test_results),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
