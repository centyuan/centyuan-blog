#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-8 下午5:17

import xadmin
from .models import CategoriesModel

class CategoriesAdminx(object):
    list_display=['name','created_time','numbers','get_num']
    search_fields=['name','numbers']
    list_filter=['name','created_time','numbers']

xadmin.site.register(CategoriesModel,CategoriesAdminx)