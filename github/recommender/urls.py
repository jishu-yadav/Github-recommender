from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('repo',views.repo_res,name='repo_res'),
    path('form',views.form_res,name='form_res'),
    path('contriform',views.form_contributors_res,name='form_contributors_res'),
]