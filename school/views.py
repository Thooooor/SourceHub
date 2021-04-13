from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import School


@login_required(login_url="/user/sign-in/")
def school_list(request):
    schools = School.objects.all()
    context = {
        "page": "school",
        "sub_page": "school_list",
        "schools": schools
    }

    return render(request, "school/school-list.html", context)


@login_required(login_url="/user/sign-in/")
def school_detail(request, id):
    school = School.objects.get(school_id=id)
    teachers = school.teachers.all()
    students = school.students.all()
    courses = school.courses.all()
    context = {
        "page": "school",
        "sub_page": "school_detail",
        "school": school,
        "teachers": teachers,
        "students": students,
        "courses": courses,
    }

    return render(request, "school/school-detail.html", context)
