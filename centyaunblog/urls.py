"""centyaunblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import  TemplateView#处理静态文件
from users.views import LoginView,Register,ActiveUserView
from django.conf.urls import url
from django.views.static import serve#处理静态文件
from centyaunblog.settings import MEDIA_ROOT
from blogs.views import BlogView,ArchiveView,Blog_detailView,Blog_searchView
from categories.views import CategoriesView,Categories_detailView
from tags.views import TagsView
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import xadmin

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',BlogView.as_view()),
    path('admin/',xadmin.site.urls),
    path('home/',TemplateView.as_view(template_name='index.html'),name='home'),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',Register.as_view(),name="register"),
    path('captcha/',include('captcha.urls')),
    #url('^active/(?P<active_code>.*)/$',ActiveUserView.as_view()),
    #re_path使用正则表达式
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view()),
    #处理上传文件url
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

    path('blog/',BlogView.as_view(),name='blog'),
    path('categories/',CategoriesView.as_view(),name='categories'),
    path('tags/',TagsView.as_view(),name='tags'),
    path('archive/',ArchiveView.as_view(),name='archive'),
    url(r'^categories/detail/(?P<cate_id>.*)$',Categories_detailView.as_view(),name='cate_detail'),
    url(r'^blog/detail/(?P<blog_id>.*)$',Blog_detailView.as_view(),name='blog_detail'),
    url(r'^search/',Blog_searchView.as_view(),name='search_blog'),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^mdeditor/',include('mdeditor.urls')),#富文档编辑器
    url(r'^go_to/$',RedirectView.as_view(url='http://www.baidu.com',),name='')#重定向默认永久

]
#meditor

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#全局404页面配置
handler404=''
handler500=''