from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from course.models import Course
from source.models import Source
from user.models import Profile


@login_required(login_url="/user/sign-in/")
def index(request):
    user = request.user
    hot_sources, max_downloads = get_hot_sources()
    hot_courses, max_students = get_hot_courses()
    max_courses, max_course_sources = get_max_courses()

    profile = Profile.objects.get(user=user)
    context = {
        "profile": profile,
        "page": "home",
        "hot_sources": hot_sources,
        "max_downloads": max_downloads,
        "hot_courses": hot_courses,
        "max_students": max_students,
        "max_courses": max_courses,
        "max_course_sources": max_course_sources
    }
    return render(request, "home/index.html", context)


def error_page(request, message):
    context = {
        "message": message,
    }

    return render(request, "home/error-page.html", context)


def get_hot_sources():
    hot_sources = Source.objects.order_by("-download_counts")
    if len(hot_sources) == 0:
        return hot_sources, 0
    max_downloads = hot_sources[0].download_counts
    if len(hot_sources) > 7:
        hot_sources = hot_sources[:7]

    return hot_sources, max_downloads


def get_hot_courses():
    hot_courses = list(Course.objects.all())
    if len(hot_courses) == 0:
        return hot_courses, 0
    hot_courses.sort(key=lambda course: course.students.count(), reverse=True)
    max_students = hot_courses[0].students.count()
    if len(hot_courses) > 7:
        hot_courses = hot_courses[:7]

    return hot_courses, max_students


def get_max_courses():
    max_courses = list(Course.objects.all())
    if len(max_courses) == 0:
        return max_courses, 0
    max_courses.sort(key=lambda course: course.sources.count(), reverse=True)
    max_course_sources = max_courses[0].students.count()
    if len(max_courses) > 7:
        max_courses = max_courses[:7]

    return max_courses, max_course_sources
