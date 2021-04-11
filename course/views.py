from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CoursePostForm
from .models import Course
from user.models import Teacher


@login_required(login_url="/user/sign-in/")
def course_list(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
        "page": "course",
        "sub_page": "course_list",
    }

    return render(request, "course/course-list.html", context)


@login_required(login_url="/user/sign-in/")
def course_post(request):
    if request.method == "POST":
        course_post_form = CoursePostForm(data=request.POST)
        if course_post_form.is_valid():
            data = course_post_form.cleaned_data
            course_name = data["course_name"]
            teacher_names = data["teacher_names"]
            print(teacher_names)
            if check_course(course_name) is False:
                return HttpResponse("已有该课程，请勿重复添加。")
            new_course = Course()
            new_course.course_name = course_name
            new_course.save()
            return redirect(to="course:course_list")
        else:
            return HttpResponse("注册表单有误，请重新输入。")
    elif request.method == "GET":
        course_post_form = CoursePostForm()
        teachers = Teacher.objects.all()
        context = {
            "form": course_post_form,
            "teachers": teachers,
            "page": "course",
            "sub_page": "course_post"
        }
        return render(request, "course/course-post.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据。")


def check_course(course_name):
    courses = Course.objects.all()
    for course in courses:
        if course.course_name == course_name:
            return False
    return True
