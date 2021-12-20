from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('repo',views.repo_rec,name='repo_rec'),
    path('form',views.form_res,name='form_res'),
    path('contriform',views.form_contributors_res,name='form_contributors_res'),
    path('user',views.user_rec,name='user_rec')
]