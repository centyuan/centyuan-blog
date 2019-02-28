from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

from .models import BlogModel,UseripNum,DayNumber
import markdown

class BlogView(View):
    #@cache_page(60*15)
    def get(self,request):
        all_blog = BlogModel.objects.all().order_by('-upload_time')
        read_rank=all_blog.order_by('-click_nums')[:10]
        new_rank=all_blog[:10]
        #blog_numbers = all_blog.count()  # 博客数量
        day_visit = DayNumber.objects.all().order_by('-day')[:7]
        data_d=[]
        data_c=[]
        for item in day_visit:
            data_d.append(str(item.day))
            data_c.append(str(item.count))

        #分页实现
        try:
            page=request.GET.get('page',1)
        except PageNotAnInteger:
            page=1
        p=Paginator(all_blog,4,request=request)
        blogs=p.page(page)
        return render(request,'index.html',{
            "all_blog":blogs,
            "read_rank":read_rank,
            "new_rank":new_rank,
            "data_d":data_d,
            "data_c":data_c
        })


class ArchiveView(View):
    def get(self,request):
        arch_blog=BlogModel.objects.all().order_by("-upload_time")
        arch_num=arch_blog.count()

        # 分页实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(arch_blog, 5, request=request)
        arblogs = p.page(page)

        return render(request,'archive.html',{
            "arch_blog":arblogs,
            "arch_num":arch_num,
        })

class Blog_detailView(View):
      def get(self,request,blog_id):
          blog=BlogModel.objects.get(id=int(blog_id))
          blog.click_nums += 1
          blog.save()
          change_num(request)
          blog.content=markdown.markdown(blog.content,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.toc',
                                  ],)
          context={'blog':blog}
          return render(request,'blog_detail.html',context)

class Blog_searchView(View):
    def get(self,request):
        # blog搜索
        search_keywords = request.GET.get('keyword', '')
        all_blog = BlogModel.objects.all().order_by('-upload_time')
        if search_keywords:
            search_blog = all_blog.filter(title__icontains=search_keywords)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(search_blog, 4, request=request)
        search_blog = p.page(page)

        return render(request, 'search_blog.html', {
            "search_blog": search_blog,

        })

#基于函数的视图用法
# return HttpResponse('hello world')
# return render(request,'blog.html',{})
# return render_to_response('blog.html',{})
#基于类的通用视图 TemplateView,listView,DetailView

def change_num(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        client_ip=request.META['HTTP_X_FORWARDED_FOR']
        client_ip=client_ip.split(',')[0]
    else:
        client_ip=request.META['REMOTE_ADDR']
    #UseripNum.objects.get()记录不存在会报错,多条记录1也会报错
    #filter返回一个对象列表
    exist_ip=UseripNum.objects.filter(ip=str(client_ip))
    if exist_ip:
        num_obj=exist_ip[0]
        num_obj.numbers +=1
    else:
        num_obj=UseripNum()
        num_obj.ip=client_ip
        num_obj.numbers=1

    num_obj.save()
    date=timezone.now().date()
    today=DayNumber.objects.filter(day=date)
    if today:
        temp=today[0]
        temp.count +=1
    else:
        temp=DayNumber()
        temp.day=date
        temp.count=1
    temp.save()

def Daytask():
    temp=DayNumber()
    temp.save()


