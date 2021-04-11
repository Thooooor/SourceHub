# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   forms.py
@Time       :   2021/4/10 18:10
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""
from django import forms

from .models import Source
from course.models import Course


class SourcePostForm(forms.ModelForm):
    source_name = forms.CharField()
    course_names = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_names'].queryset = Course.objects.all()

    class Meta:
        model = Source
        fields = ("source_name", "source_file")
