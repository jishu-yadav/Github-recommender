from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from .Recommendersys import *
from .models import Repository
import pandas as pd
# Create your views here.
def index(request):
    return render(request,'index.html')

def repo_rec(request):
    #model=joblib.load("repo_model")
    df=pd.DataFrame((list(Repository.objects.all().values())))
    #print(df.head())
    dictionary,tfidf,index,lsi=fit(df['content'])
    #print(cosine_sim)
    repo_list=recommendations(dictionary,tfidf,index,lsi,"sample code for several design patterns in PHP 8 ['code-examples', 'design-pattern', 'design-patterns', 'designpatternsphp', 'hacktoberfest', 'modern-php', 'oop', 'php', 'php8', 'phpunit'] dict_keys(['PHP', 'Python', 'Makefile', 'Dockerfile'])")
    print(repo_list)

    #list_repo=model.recommendations("sample code for several design patterns in PHP 8 ['code-examples', 'design-pattern', 'design-patterns', 'designpatternsphp', 'hacktoberfest', 'modern-php', 'oop', 'php', 'php8', 'phpunit'] dict_keys(['PHP', 'Python', 'Makefile', 'Dockerfile'])")
    #print(list_repo)
    return render(request,'repo_rec.html')

def form_contributors_res(request):
    return render(request,'form_contributors.html')
    
def form_res(request):
    return render(request,'form.html')

def user_rec(request):
    return render(request,'user_rec.html')
