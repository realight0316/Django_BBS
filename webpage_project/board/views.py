from django.shortcuts import render
from board.forms import *

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        form.company_id = request.user
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})

def board(request):
    articleList = Article.objects.all()
    return render(request, 'board.html', {'articleList': articleList})

def view(request, num="1"):
    article = Article.objects.get(post_id=num)

    return render(request, 'list.html', {'article':article})
