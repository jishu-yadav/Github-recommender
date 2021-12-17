from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def repo_res(request):
    return render(request,'repo_rec.html')

