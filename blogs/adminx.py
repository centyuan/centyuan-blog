#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-8 下午5:16
import xadmin
from .models import BlogModel,UseripNum,DayNumber
from xadmin import  views
from mdeditor.fields import MDTextField

class GlobalSettings(object):
    site_title='centyuan'
    site_footer='centyuan'
    menu_style='accordion'

class BlogAminx(object):
    #显示的列表项
    list_display=['title','upload_time','category','tag','click_nums','visit_num']
    #可搜索的列表项
    search_fields=['title','category','tag','click_nums','visit_num']
    #筛选字段
    list_filter=['title','upload_time','category','tag','click_nums','visit_num']

    style_fields = {"content": "ueditor"}
    def save_models(self):
        #新增和修改都会做操作
        #在保存blog时统计该blog分类下blog数量
        obj=self.new_obj
        obj.save()#先保存再统计
        if obj.category is not None:
            cate=obj.category
            cate.numbers=BlogModel.objects.filter(category=cate).count()
            cate.save()
        if obj.tag is not None:
            tag=obj.tag
            tag.number=BlogModel.objects.filter(tag=tag).count()
            tag.save()
class UseripNumAdminx(object):
    list_display=['ip','numbers','time']
    search_fields=['ip','numbers','time']
    list_filter=['ip','numbers','time']

class DayNumberAdminx(object):
    list_display=['day','count']
    search_fields=['day','count']
    list_filter=['day','count']


xadmin.site.register(BlogModel,BlogAminx)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(UseripNum,UseripNumAdminx)
xadmin.site.register(DayNumber,DayNumberAdminx)