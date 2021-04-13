import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from course.models import Course
from home.views import error_page
from .forms import SourcePostForm
from .models import Source


@login_required(login_url="/user/sign-in/")
def source_list(request, search=None):
    if "search" in request.GET.keys():
        search = request.GET["search"]
        sources = search_source(search)
    else:
        sources = Source.objects.order_by("-download_counts", "-upload_time")

    context = {
        "page": "source",
        "sub_page": "source_list",
        "sources": sources,
        "search": search
    }

    return render(request, "source/source-list.html", context)


@login_required(login_url="/user/sign-in/")
def source_post(request):
    user = request.user
    if request.method == "POST":
        source_post_form = SourcePostForm(request.POST, request.FILES)
        print(source_post_form.errors)
        if source_post_form.is_valid():
            form_data = source_post_form.cleaned_data
            source_name = form_data["source_name"]
            course_names = form_data["course_names"]
            new_source = Source()
            new_source.source_name = source_name
            new_source.upload_user = user
            if 'source_file' in request.FILES:
                new_source.source_file = form_data["source_file"]
            new_source.save()
            for course in course_names:
                course.sources.add(new_source)
                course.save()
            return redirect(to="source:source_list")
        else:
            return error_page(request, "表单内容有误，请重新填写。")
    elif request.method == "GET":
        source_post_form = SourcePostForm()
        courses = Course.objects.all()
        course_list = []
        for i, course in enumerate(courses):
            name = course.course_name
            id = "id_course_names_%d" % i
            course_list.append(CourseItem(name, course.course_id, id))
        context = {
            "form": source_post_form,
            'course_list': course_list,
            "page": "source",
            "sub_page": "source_post"
        }
        return render(request, "source/source-post.html", context)
    else:
        return error_page(request, "请使用GET或POST请求数据。")


@login_required(login_url="/user/sign-in/")
def source_delete(request, id):
    user = request.user
    source = Source.objects.get(source_id=id)
    if user != source.upload_user:
        return error_page(request, "你没有进行该操作的权限。")
    file_path = source.source_file.path
    Source.delete(source)
    os.remove(file_path)
    return redirect(to="source:source_list")


@login_required(login_url="/user/sign-in/")
def source_download_count(request):
    id = request.GET.get('id')
    source = Source.objects.get(source_id=id)
    source.download_counts += 1
    source.save()
    return redirect("source:source_list")


class CourseItem:
    def __init__(self, name, value, id):
        self.name = name
        self.value = value
        self.id = id


def search_source(search):
    sources = Source.objects.order_by("-download_counts", "-upload_time")
    results = []
    for source in sources:
        if search in source.source_name:
            results.append(source)
        elif search in source.upload_user.username:
            results.append(source)
        else:
            for course in source.courses.all():
                if search in course.course_name:
                    results.append(source)
                    break
    return results
