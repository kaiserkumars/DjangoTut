from django.urls import path 
from . import views #the dot makes python search for all the file names with views in any folder at accounts level

from django.contrib.auth.views import login

urlpatterns = [
path('',views.home,name='home'),
path('login/',login,{'template_name':'accounts/login.html'}),#specifying the object template_name here makes it possible to create our own login.html page rathr than the default one.
]