from django.shortcuts import render
from django.views.generic.base import View
from .models import CategoriesModel
from blogs.models import BlogModel
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger


class CategoriesView(View):
    def get(self,request):
        all_cate=CategoriesModel.objects.all()
        cate_num=all_cate.count()
        return render(request,'category.html',{
            "all_cate":all_cate,
            "cate_num":cate_num,
        })

class Categories_detailView(View):
    def get(self,request,cate_id):
        cate_blog=BlogModel.objects.all().filter(category_id=int(cate_id)).order_by('-upload_time')
        try:
            page=request.GET.get('page',1)
        except PageNotAnInteger:
            page=1
        p=Paginator(cate_blog,2,request=request)
        cate_blogs=p.page(page)

        return render(request,'category_detail.html',{
            "cate_blogs":cate_blogs,
        })
