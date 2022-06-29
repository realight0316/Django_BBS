from distutils.log import error
from django.forms import ModelForm
from board.models import *
from django import forms

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['position_name', 'awards',  'contents', 'skills', 'write_date']

class articleForm(forms.Form):
    position_name = forms.CharField(error_messages={'required': "포지션명을 입력하시오"}, lebel = '포지션명', max_length=50)
    contents = forms.CharField(error_messages={'required':'내용을 입력하시오'}, label="채용내용", widget= forms.Textarea)
    awards = forms.IntegerField(error_messages={'required': "보상금을 입력하시오"}, label="채용보상금")