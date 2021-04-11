# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   forms.py
@Time       :   2021/4/11 11:10
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""
from django import forms
from .models import Course


class CoursePostForm(forms.ModelForm):
    course_name = forms.CharField()
    teacher_names = forms.CharField()

    class Meta:
        model = Course
        fields = ('course_name',)
