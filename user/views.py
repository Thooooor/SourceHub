from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserSignInForm, UserSignUpForm
from .models import Message, Profile, Student, Teacher


def user_sign_in(request):
    user = request.user

    if user.is_authenticated:
        return redirect(to="home:index")

    if request.method == 'POST':
        user_sign_in_form = UserSignInForm(data=request.POST)
        if user_sign_in_form.is_valid():
            data = user_sign_in_form.cleaned_data
            username = User.objects.get(Q(email=data["email"]))
            user = authenticate(username=username, password=data["password"])
            if user:
                login(request, user)
                return redirect(to="home:index")
            else:
                return HttpResponse("账号或密码输入有误。请重新输入.")
        else:
            return HttpResponse("账号或密码输入不合法。")
    elif request.method == 'GET':
        user_sign_in_form = UserSignInForm()
        context = {'form': user_sign_in_form}
        return render(request, 'user/sign-in.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据。")


def user_sign_up(request):
    user = request.user
    if user.is_authenticated:
        return redirect(to="home:index")
    if request.method == 'POST':
        user_sign_up_form = UserSignUpForm(data=request.POST)
        if user_sign_up_form.is_valid():
            form_data = user_sign_up_form.cleaned_data
            print(form_data)
            username = form_data["username"]
            email = form_data["email"]
            user_type = form_data["user_type"]
            if check_email(email) is False:
                return HttpResponse("该邮箱已经被注册。")
            new_user = User()
            new_user.username = username
            new_user.email = email
            new_user.set_password(user_sign_up_form.cleaned_data["password"])
            new_user.save()
            print(Profile.objects.all())
            profile = Profile()
            profile.user = new_user
            profile.user_type = user_type
            profile.save()
            if user_type == "student":
                student_id = form_data["user_id"]
                new_student = Student()
                new_student.user = new_user
                new_student.student_id = student_id
                new_student.student_name = username
                new_student.save()
            else:
                teacher_id = form_data["user_id"]
                new_teacher = Teacher()
                new_teacher.user = new_user
                new_teacher.teacher_id = teacher_id
                new_teacher.teacher_name = username
                new_teacher.save()
            return redirect(to="home:index")
        else:
            return HttpResponse("注册表单有误。请重新输入。")
    elif request.method == 'GET':
        user_sign_up_form = UserSignUpForm()
        context = {"form": user_sign_up_form}
        return render(request, 'user/sign-up.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据。")


@login_required(login_url="/user/sign-in/")
def sign_out(request):
    logout(request)
    return redirect(to="user:sign-in")


@login_required(login_url="/user/sign-in/")
def delete_user(request):
    user = User.objects.get(id=id)
    if request.user == user:
        logout(request)
        user.delete()
        return redirect(to="user:sign-in")
    else:
        return HttpResponse("你没有删除操作的权限")


def user_info(request):
    context = {}

    return render(request, "", context)


def message_detail(request, id):
    Message.objects.get(id=id)
    context = {}

    return render(request, "", context)


def check_email(email):
    users = User.objects.all()

    for user in users:
        if user.email == email:
            return False
    return True
