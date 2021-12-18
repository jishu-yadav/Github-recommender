from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('repo',views.repo_rec,name='repo_res'),
    path('user',views.user_rec,name='repo_rec')
]