#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-11 下午4:23

from django import  forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    #required=True 必填字段

    usernmae=forms.CharField(required=True,max_length=15)
    password=forms.CharField(required=True)

class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True)
    captcha=CaptchaField(error_messages={"invalid":"验证码错误"})
    #error_messages={"invalid":"验证码错误"}自定义错误类型

