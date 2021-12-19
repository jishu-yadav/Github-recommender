from django.db import models
from separatedvaluesfield.models import SeparatedValuesField
# Create your models here.
class Repository(models.Model):
    
    full_name=models.CharField(max_length=500,blank=True)
    owner_name=models.CharField(max_length=500,blank=True)
    repo_url=models.URLField(max_length=500,blank=True)
    homepage=models.URLField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(blank=True,null=True)
    watchers=models.IntegerField(default=0)
    open_issues=models.IntegerField(default=0)
    forks_count=models.IntegerField(default=0)
    stargazers_count=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    topics=models.TextField(blank=True)
    language=models.TextField(blank=True)
    content=models.TextField(blank=True)
    


