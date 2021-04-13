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

    for source in hot_sources:
        if source.download_counts > 0:
            source.ratio = source.download_counts / max_downloads * 86

    return hot_sources, max_downloads


def get_hot_courses():
    hot_courses = list(Course.objects.all())
    if len(hot_courses) == 0:
        return hot_courses, 0
    hot_courses.sort(key=lambda hot_course: hot_course.students.count(), reverse=True)
    max_students = hot_courses[0].students.count()
    if len(hot_courses) > 7:
        hot_courses = hot_courses[:7]

    for course in hot_courses:
        if course.students.count() > 0:
            course.ratio = course.students.count() / max_students * 70

    return hot_courses, max_students


def get_max_courses():
    max_courses = list(Course.objects.all())
    if len(max_courses) == 0:
        return max_courses, 0
    max_courses.sort(key=lambda max_course: max_course.sources.count(), reverse=True)
    max_course_sources = max_courses[0].students.count()
    if len(max_courses) > 7:
        max_courses = max_courses[:7]

    for course in max_courses:
        if course.sources.count() > 0:
            course.ratio = course.sources.count() / max_course_sources * 80

    return max_courses, max_course_sources
