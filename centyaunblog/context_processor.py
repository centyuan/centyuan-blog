#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-16 下午8:40
#上下文渲染器 在多个模板中使用都可以使用同一个变量
from blogs.models import BlogModel
from categories.models import CategoriesModel
from tags.models import TagModel

def info_num(request):
    num_blog=BlogModel.objects.all().count()
    num_category=CategoriesModel.objects.all().count()
    num_tag=TagModel.objects.all().count()

    return {'num_blog':num_blog,'num_category':num_category,'num_tag':num_tag}