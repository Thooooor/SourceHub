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


class SourcePostForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ("source_name", "courses", "file")
