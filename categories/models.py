from django.db import models
from django.utils import  timezone

class CategoriesModel(models.Model):
    name=models.CharField(max_length=50,verbose_name='分类名称')
    created_time=models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    numbers=models.IntegerField(default=0,verbose_name='博客数')

    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name

    def get_num(self):
        #获取blog数量
        return self.blogmodel_set.all().count()
    #后台显示名称
    get_num.short_description="数量"

    def __str__(self):
        return self.name

