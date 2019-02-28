from django.db import models
from django.utils import  timezone

class TagModel(models.Model):
    name=models.CharField(max_length=50,verbose_name='标签名称')
    created_time=models.DateTimeField(default=timezone.now,verbose_name='创建时间')
    number=models.IntegerField(default=0,verbose_name='博客数')

    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name

    def get_num(self):
        return self.blogmodel_set.count()
    get_num.short_description="数量"

    def __str__(self):
        return self.name