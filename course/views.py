from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CoursePostForm
from .models import Course
from user.models import Teacher, Profile


@login_required(login_url="/user/sign-in/")
def course_list(request):
    user = request.user
    courses = Course.objects.all()
    profile = Profile.objects.get(user=user)
    context = {
        "courses": courses,
        "profile": profile,
        "page": "course",
        "sub_page": "course_list",
    }

    return render(request, "course/course-list.html", context)


@login_required(login_url="/user/sign-in/")
def course_post(request):
    user = request.user
    if user.profile.user_type == "student":
        return HttpResponse("对不起，你没有权限进行该操作。")
    if request.method == "POST":
        course_post_form = CoursePostForm(data=request.POST)
        if course_post_form.is_valid():
            data = course_post_form.cleaned_data
            course_name = data["course_name"]
            course_status = data["course_status"]
            teacher_names = data["teacher_names"]
            if check_course(course_name) is False:
                return HttpResponse("已有该课程，请勿重复添加。")
            new_course = Course()
            new_course.course_name = course_name
            new_course.course_status = course_status
            new_course.save()
            for teacher in teacher_names:
                teacher.courses.add(new_course)
                teacher.save()
            return redirect(to="course:course_list")
        else:
            return HttpResponse("注册表单有误，请重新输入。")
    elif request.method == "GET":
        course_post_form = CoursePostForm()
        teachers = Teacher.objects.all()
        teacher_list = []
        for i, teacher in enumerate(teachers):
            name = teacher.teacher_name
            id = "id_teacher_names_%d" % i
            teacher_list.append(TeacherItem(name, i+1, id))
        context = {
            "form": course_post_form,
            "teacher_list": teacher_list,
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


class TeacherItem:
    def __init__(self, name, value, id):
        self.value = value
        self.name = name
        self.id = id
