from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
#로그인에 필요 어센티케이션은 매개변수 2개받음
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# 로그아웃에 필요
from django.contrib.auth import logout as auth_logout

#로그인 데코레이터(비로그인 입구컷)
from django.contrib.auth.decorators import login_required

#회원가입양식
from django.contrib.auth.forms import UserCreationForm

#회원정보 수정양식
from django.contrib.auth.forms import UserChangeForm
from .forms import CustomUserChangeForm

#비번변경
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('app1:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) #이건 외워야함 로그인로직
            return redirect(request.GET.get('next') or 'app1:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('app1:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('app1:index')
    else :
        form = UserCreationForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)
@login_required
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        #주의할점: 탈퇴후 로그아웃 이순서 해야함 
        # (혹시라도 회원탈퇴하고 로그아웃 안되는경우에)
    return redirect('app1:index')
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('app1:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)
@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('app1:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html',context)