# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   urls.py
@Time       :   2021/4/9 23:26
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""
from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path("list/", views.course_list, name="course_list")
]
