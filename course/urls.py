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
    path("course-list", views.course_list, name="course_list"),
    path("course-post/", views.course_post, name="course_post"),
    path("course-status-change/<int:id>/", views.course_status_change, name="course_status_change"),
    path("course-pick/<int:id>/", views.course_pick, name="course_pick"),
    path("course-drop/<int:id>/", views.course_drop, name="course_drop"),
    path("course-delete/<int:id>/", views.course_delete, name="course_delete"),
]
