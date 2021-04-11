from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.apps import apps

from .models import Source
from .forms import SourcePostForm


def source_list(request):
    context = {
        "page": "source",
        "sub_page": "source_list"
    }

    return render(request, "source/source-list.html", context)


@login_required(login_url="/user/login/")
def source_post(request):
    if request.method == "POST":
        source_post_form = SourcePostForm(data=request.POST)

        if source_post_form.is_valid():
            form_data = source_post_form.cleaned_data
            new_source = Source()
            new_source.source_name = form_data["source_name"]
            if 'file' in request.FILES:
                new_source.file = form_data["file"]
            new_source.save()
            return redirect(to="source:list")
        else:
            return HttpResponse("表单内容有误，请重新填写。")


def source_detail(request):
    context = {}

    return render(request, "source/source-detail.html", context)
