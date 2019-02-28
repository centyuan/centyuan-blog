#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-8 下午5:20
import xadmin
from .models import TagModel

class TagAdminx(object):
    list_display=['name','created_time','number','get_num']
    search_fields=['name','number']
    list_filter=['name','created_time','number']


xadmin.site.register(TagModel,TagAdminx)