from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import AbstractBaseUser
#只含有 password, last_login is_active
from datetime import datetime

class UserProfile(AbstractUser):
    nick_name=models.CharField(verbose_name='昵称',max_length=50,default='')
    birthday=models.DateField(verbose_name='生日',blank=True,null=True)
    gender=models.CharField(verbose_name='性别',max_length=6,choices=(('male','男'),('female','女')))
    address=models.CharField(verbose_name='地址',max_length=100)
    mobile=models.CharField(max_length=11,blank=True,null=True)
    image=models.ImageField(verbose_name='头像',upload_to='image/%Y/%m',default='imgae/default.png',max_length=100)

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name='验证码')
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    send_type=models.CharField(verbose_name='验证码类型',choices=(('register','注册'),('forget','找回密码'),('update_email','修改邮箱')),max_length=30)
    send_time=models.DateTimeField(verbose_name='发送时间',default=datetime.now)

    class Meta:
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name

    def __str__(self):
        return  '{0}({1})'.format(self.code,self.email)

