from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from school.models import School
from .forms import CoursePostForm
from .models import Course
from user.models import Teacher, Profile
from home.views import error_page


@login_required(login_url="/user/sign-in/")
def course_list(request, search=None):
    if "search" in request.GET.keys():
        search = request.GET["search"]
        courses = search_course(search)
    else:
        courses = Course.objects.order_by("-course_status", "school")

    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        "courses": courses,
        "profile": profile,
        "page": "course",
        "sub_page": "course_list",
        "search": search,
    }

    return render(request, "course/course-list.html", context)


@login_required(login_url="/user/sign-in/")
def course_post(request):
    user = request.user
    if user.profile.user_type == "student":
        return error_page(request, "对不起，你没有权限进行该操作。")
    if request.method == "POST":
        course_post_form = CoursePostForm(data=request.POST)
        if course_post_form.is_valid():
            data = course_post_form.cleaned_data
            course_name = data["course_name"]
            course_status = data["course_status"]
            school_name = data["school_name"]
            teacher_names = data["teacher_names"]
            if check_course(course_name) is False:
                return error_page(request, "已有该课程，请勿重复添加。")
            new_course = Course()
            new_course.course_name = course_name
            new_course.course_status = course_status
            new_course.save()
            school = School.objects.get(school_name=school_name)
            school.courses.add(new_course)
            school.save()
            for teacher in teacher_names:
                teacher.courses.add(new_course)
                teacher.save()
            return redirect(to="course:course_list")
        else:
            return error_page(request, "注册表单有误，请重新输入。")
    elif request.method == "GET":
        course_post_form = CoursePostForm()
        teachers = Teacher.objects.all()
        teacher_list = []
        for i, teacher in enumerate(teachers):
            name = teacher.teacher_name
            id = "id_teacher_names_%d" % i
            teacher_list.append(TeacherItem(name, teacher.id, id))
        schools = School.objects.all()
        school_list = []
        for i, school in enumerate(schools):
            name = school.school_name
            id = "id_teacher_names_%d" % i
            school_list.append(TeacherItem(name, school.school_id, id))
        context = {
            "form": course_post_form,
            "teacher_list": teacher_list,
            "school_list": school_list,
            "page": "course",
            "sub_page": "course_post"
        }
        return render(request, "course/course-post.html", context)
    else:
        return error_page(request, "请使用GET或POST请求数据。")


@login_required(login_url="/user/sign-in/")
def course_delete(request, id):
    user = request.user
    if user.profile.user_type == "student":
        return error_page(request, "你没有进行该操作的权限。")
    course = Course.objects.get(course_id=id)
    if user.teacher not in course.teachers.all():
        return error_page(request, "你没有进行该操作的权限。")
    Course.delete(course)
    return redirect(to="course:course_list")


@login_required(login_url="/user/sign-in/")
def course_status_change(request, id):
    user = request.user
    if user.profile.user_type == "student":
        return error_page(request, "你没有进行该操作的权限。")
    course = Course.objects.get(course_id=id)
    if user.teacher not in course.teachers.all():
        return error_page(request, "你没有进行该操作的权限。")

    if course.course_status == "close":
        course.course_status = "open"
    else:
        course.course_status = "close"
    course.save()

    return redirect(to="course:course_list")


@login_required(login_url="/user/sign-in/")
def course_pick(request, id):
    user = request.user
    course = Course.objects.get(course_id=id)
    if user.profile.user_type == "student":
        if user.student not in course.students.all():
            user.student.courses.add(course)
            user.student.save()
        else:
            return error_page(request, "你已经选择了该课程。")
    else:
        if user.teacher not in course.teachers.all():
            user.teacher.courses.add(course)
            user.teacher.save()
        else:
            return error_page(request, "你已经在教授该课程。")
    return redirect(to="course:course_list")


@login_required(login_url="/user/sign-in/")
def course_drop(request, id):
    user = request.user
    course = Course.objects.get(course_id=id)
    if user.profile.user_type == "student":
        if user.student in course.students.all():
            user.student.courses.remove(course)
            user.student.save()
        else:
            return error_page(request, "你没有选择该课程。")
    else:
        if user.teacher in course.teachers.all():
            user.teacher.courses.remove(course)
            user.teacher.save()
        else:
            return error_page(request, "你没有教授该课程。")
    return redirect(to="course:course_list")


def check_course(course_name):
    courses = Course.objects.all()
    for course in courses:
        if course.course_name == course_name:
            return False
    return True


def search_course(search):
    courses = Course.objects.order_by("-course_status", "school")
    result = []
    for course in courses:
        if search in course.course_name:
            result.append(course)
        elif search in ["开课", "已开课"] and course.course_status == "open":
            result.append(course)
        elif search in ["结课", "未开课"] and course.course_status == "close":
            result.append(course)
        elif search in course.school.school_name:
            result.append(course)
        else:
            for teacher in course.teachers.all():
                if search in teacher.teacher_name:
                    result.append(course)
                    break
    return result


class TeacherItem:
    def __init__(self, name, value, id):
        self.value = value
        self.name = name
        self.id = id
