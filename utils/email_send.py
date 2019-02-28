#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-11 下午6:55
from random import Random
from django.core.mail import send_mail#发送邮件

from users.models import EmailVerifyRecord
from centyaunblog.settings import DEFAULT_FROM_EMAIL
def random_str(randomlength=8):
    #产生随机字符串
    str=""
    chars="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length=len(chars)-1
    random=Random()
    for i in range(randomlength):
        str +=chars[random.randint(0,length)]
    return str



def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code=code
    email_record.email=email
    email_record.send_type=send_type
    email_record.save()
    email_title=""
    email_boby=""

    if send_type == "register":
        email_title="centyuan邮箱激活注册链接:"
        email_boby="请点击一下链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)
        send_status=send_mail(email_title,email_boby,DEFAULT_FROM_EMAIL,[email])
        #最后一个参数为接受邮件列表
        if send_status:
            pass
