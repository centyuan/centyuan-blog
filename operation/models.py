from django.db import models
from datetime import  datetime

from users.models import UserProfile
from blogs.models import BlogModel

class UserComments(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    blog=models.ForeignKey(BlogModel,verbose_name='博客',on_delete=models.CASCADE)
    comments=models.CharField(max_length=200,verbose_name='评论',)
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name='用户评论'
        verbose_name_plural=verbose_name

class UserFavorite(models.Model):
    user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    blog=models.ForeignKey(BlogModel,verbose_name='博客',on_delete=models.CASCADE)
    add_time=models.DateTimeField(default=datetime.now,verbose_name='收藏时间')

    class Meta:
        verbose_name='用户收藏'
        verbose_name_plural=verbose_name