"""plus2net URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
#from .student import views # . represents the directory this script is in

#import student


from django.conf import settings

from django.conf.urls import url
from student import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home), #first argument specifies the url name after localhost
    path('hello_world', views.hello_world), #first argument specifies the url name after localhost 
    path('display', views.display), #first argument specifies the url name after localhost 
    path("people", views.PersonListView.as_view())
] 

