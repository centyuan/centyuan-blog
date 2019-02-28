from django.shortcuts import render
from django.views.generic.base import View
from .models import TagModel

class TagsView(View):
    def get(self,request):
        all_tags=TagModel.objects.all()
        tags_num=all_tags.count()

        return render(request,'tags.html',{
            "all_tags":all_tags,
            "tags_num":tags_num,
        })
