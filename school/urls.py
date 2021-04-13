# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   urls.py
@Time       :   2021/4/13 0:49
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""
from django.urls import path

from . import views

app_name = "school"

urlpatterns = [
    path("school-list/", views.school_list, name="school-list"),
    path("school-detail/<int:id>/",views.school_detail, name="school-detail"),

]
