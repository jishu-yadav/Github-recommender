from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('repo',views.repo_res,name='repo_res')
]