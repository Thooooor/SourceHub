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
from user.models import Teacher


class CoursePostForm(forms.ModelForm):
    course_name = forms.CharField()
    course_status = forms.CharField(empty_value='close')
    teacher_names = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher_names'].queryset = Teacher.objects.all()

    class Meta:
        model = Course
        fields = ('course_name',)
