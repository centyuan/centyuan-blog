#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-9 下午4:58
import xadmin
from .models import UserProfile

class UserProfileAdmin(object):
    list_display = ['username','nick_name','gender','mobile']
    search_fields = ['username','nick_name','gender','mobile']
    list_filter = ['username','nick_name','gender','mobile']


#xadmin.site.register(UserProfile,UserProfileAdmin)