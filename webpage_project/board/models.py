import re
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    post_id = models.AutoField(verbose_name='공고id ', primary_key=True)
    company_id = models.ForeignKey('users.Users', verbose_name='회사id', on_delete=models.CASCADE)
    position_name = models.CharField(verbose_name='포지션명', max_length=50)
    awards = models.IntegerField(verbose_name='취업보상금')
    contents = models.TextField(verbose_name='채용내용')
    skills = models.CharField(verbose_name='사용기술', max_length=50)
    write_date = models.DateTimeField(verbose_name='작성일자', default=timezone.now)
    # write_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "articles"       # db테이블명 정의
        verbose_name = "채용공고 정보"

class Company(models.Model):
    company_id = models.CharField(verbose_name='회사id', max_length=30, primary_key=True)
    company_pw = models.CharField(verbose_name='회사pw', max_length=50)
    company_name = models.CharField(verbose_name='회사명', max_length=20)
    nation = models.CharField(verbose_name='국가', max_length=20)
    region = models.CharField(verbose_name='지역', max_length=20, null=True)

    def __str__(self):
        return self.company_name        # 관리자 화면에서 보이는 정보표기

    class Meta:
        db_table = "company_info"       # db테이블명 정의
        verbose_name = "회사 정보"

