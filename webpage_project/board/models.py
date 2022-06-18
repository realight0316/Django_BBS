from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    post_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    position_name = models.CharField(max_length=50)
    awards = models.IntegerField()
    contents = models.TextField()
    skills = models.CharField(max_length=50)
    write_date = models.DateTimeField(default=timezone.now)
    # write_date = models.DateTimeField(auto_now_add=True)
    # 공고문id, 회사id, 포지션명, 취업보상금, 채용내용, 사용기술, 작성일자

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
    region = models.CharField(max_length=20, null=True)
