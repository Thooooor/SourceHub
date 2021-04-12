# -*- encoding: utf-8 -*-
"""
@Project    :   SourceHub
@File       :   forms.py
@Time       :   2021/4/10 19:35
@Author     :   Thooooor
@Version    :   1.0
@Contact    :   thooooor999@gmail.com
@Describe   :   None
"""
from django import forms
from django.contrib.auth.models import User
from .models import Message


class MessagePostForm(forms.Form):
    message_title = forms.CharField()
    message_body = forms.CharField(widget=forms.Textarea)
    recv_user = forms.CharField()

    class Meta:
        model = Message
        fields = ("title", "body")


class UserSignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class UserSignUpForm(forms.Form):
    user_type = forms.CharField()
    user_id = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get("password") == data.get("password2"):
            return data.get('password')
        else:
            raise forms.ValidationError("两次密码输入不一致，请重试。")
