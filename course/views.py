from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/user/sign-in/")
def course_list(request):
    context = {}

    return render(request, "course/course-list.html", context)

