# encoding:utf-8
from django import forms


class UserRegister(forms.Form):
    user_name = forms.CharField(max_length=30,label='用户名')
    user_email = forms.EmailField(max_length=30,label='电子邮件')
    user_url = forms.URLField(max_length=30,label='url')
    user_password = forms.CharField(max_length=10,label='密码')
    user_password_sure = forms.CharField(max_length=10,label='确认密码')


class UserLogin(forms.Form):
    user_name = forms.CharField(max_length=30,label='用户名')
    user_password = forms.CharField(max_length=10,label='密码')
