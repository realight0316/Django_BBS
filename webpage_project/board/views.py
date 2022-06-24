from django.shortcuts import redirect, render
from board.forms import *
from .models import Company
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        company_name = request.POST.get('company_name', None)
        company_id = request.POST.get('company_id', None)
        company_pw = request.POST.get('company_pw', None)
        re_company_pw = request.POST.get('re_company_pw', None)
        nation = request.POST.get('nation', None)
        region = request.POST.get('region', None)
        errorMsg = {}

        if not (company_id and company_pw and re_company_pw and nation):
            errorMsg['error'] = "모든 값을 입력해야 합니다."
        elif company_pw != re_company_pw:
            errorMsg['error'] = '비밀번호가 다릅니다.'
        else:
            company_info = Company(
                company_id = company_id,
                company_pw = make_password(company_pw),
                company_name = company_name,
                nation = nation,
                region = region
            )
            company_info.save()
        return render(request, 'signup.html', errorMsg)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        company_id = request.POST.get('company_id', None)
        company_pw = request.POST.get('company_pw', None)
        errMsg = {}

        if not (company_id and company_pw):
            errMsg['error'] = '아이디와 비밀번호를 입력하시오'
        else:
            company = Company.objects.get(company_id = company_id)
            if check_password(company_pw, company.company_pw):
                request.session['company'] = company.id
                return redirect('/')
            else:
                errMsg['error'] = "비밀번호를 다시 입력하시오"
        return render(request, 'login.html', errMsg)

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
