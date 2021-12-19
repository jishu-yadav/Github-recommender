from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import json
from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.
def index(request):
    return render(request,'index.html')

def repo_rec(request):
    #model=joblib.load("repo_model")
    url=staticfiles_storage.url('repo_data.json')
    cosine_sim=open(url)
    print(cosine_sim)
    #list_repo=model.recommendations("sample code for several design patterns in PHP 8 ['code-examples', 'design-pattern', 'design-patterns', 'designpatternsphp', 'hacktoberfest', 'modern-php', 'oop', 'php', 'php8', 'phpunit'] dict_keys(['PHP', 'Python', 'Makefile', 'Dockerfile'])")
    #print(list_repo)
    return render(request,'repo_rec.html')

def user_rec(request):
    return render(request,'user_rec.html')