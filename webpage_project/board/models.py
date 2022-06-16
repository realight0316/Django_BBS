from django.db import models

# Create your models here.

class Article(models.Model):
    post_id = models.AutoField(primary_key=True)
    company_id = models.IntegerField()
    position_name = models.CharField(max_length=50)
    awards = models.IntegerField()
    contents = models.TextField()
    skills = models.CharField(max_length=50)
    write_date = models.DateTimeField(auto_now_add=True)
    # 회사id, 공고문id, 포지션명, 취업보상금, 채용내용, 사용기술, 작성일자