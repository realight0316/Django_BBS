from django.forms import ModelForm
from board.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['position_name', 'awards',  'contents', 'skills', 'write_date']