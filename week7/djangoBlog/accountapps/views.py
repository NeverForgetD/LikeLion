from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def login(request):
    #1 GET 요청이 들어오면 login.html 띄워준다
    if request.method == 'GET':
        return render(request, 'login.html')
    #1  POST 요청이 들어오면 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']

        # DB에 있는 유저인지 확인
        user = auth.authenticate(request, username=userid,password=userpw)

        if user is not None:
            auth.login(request, user)
            # 로그인 후 홈으로 돌려보내기
            return redirect('home')
        else:
            # 다시 로그인 페이지로 돌려보내기
            return render(request, 'login.html')
        
def logout(request):
    auth.logout(request) # 로그아웃
    return redirect('home')

def signup(request):
    #1 GET 요청 시 sign.html 띄워준다
    if request.method == 'GET':
        return render(request,'signup.html')
    #2 POST 요청 시 새로운 유저 객체 생성해 회원가입 시킨다
    if request.method == 'POST':
        # input 값 변수에 할당
        userid = request.POST['username']
        userpw = request.POST['password']
        # 회원가입
        new_user = User.objects.create_user(username=userid, password=userpw)
        # 로그인
        auth.login(request, new_user)
        # 홈화면으로
        return redirect('home')