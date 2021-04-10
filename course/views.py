from django.shortcuts import render


def course_list(request):
    context = {}

    return render(request, "course/course.html", context)
