from django.db import models
from django.utils import timezone
from categories.models import CategoriesModel
from tags.models import TagModel
from DjangoUeditor.models import UEditorField
from mdeditor.fields import MDTextField

class BlogModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    # upload_time=models.DateTimeField(default=datetime.now,verbose_name='创建时间')
    upload_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    category = models.ForeignKey(CategoriesModel, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ForeignKey(TagModel, verbose_name='标签', on_delete=models.CASCADE)
    introduction = models.TextField(verbose_name='引言')
    #content=models.TextField(verbose_name='正文',default='')
    click_nums=models.IntegerField(verbose_name='点击量',default=0)
    visit_num=models.IntegerField(verbose_name='访问量',default=0)
    # content=UEditorField(verbose_name='正文',default='',width=900, height=400, imagePath="blog/images/",
    #                                      filePath="blog/files/")
    content=MDTextField(verbose_name='正文',default='')
    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    # def save(self):
    #     obj = self.new_obj
    #     obj.save()  # 先保存再统计
    #     if obj.category is not None:
    #         cate=obj.category
    #         cate.numbers=BlogModel.objects.filter(category=cate).count()
    #         cate.save()
    #     if obj.tag is not None:
    #         tag=obj.tag
    #         tag.number=BlogModel.objects.filter(tag=tag).count()
    #         tag.save()

#model.CharField(verbose="分类",choices=(("cj","初级"),("zj","中级")))
#前端取值会取到数据中的值 cj,zj
#如BlogModel.object.all().category
#应写成BlogModel.object.all().get_category_display
#auto_now_add创建添加时间
# 创建或添加对象时的时间, 修改或更新对象时, 不会更改时间
# auto_now
# 凡是对对象进行操作(创建 / 添加 / 修改 / 更新), 时间都会随之改变
#更新时间
#上面两个无法在程序中手动赋值  admin显示为只读
#会导致字段成为editable=False和blank=True的状态

#如何将创建时间设置为“默认当前”并且可修改
#default=timezone.now
#
class UseripNum(models.Model):
    #ip=models.IPAddressField()

     ip=models.CharField(verbose_name='ip地址',max_length=30)
     numbers=models.IntegerField(verbose_name='访问次数')
     time=models.DateTimeField(verbose_name='最新访问时间',auto_now=True)

     class Meta:
         verbose_name='ip访问量'
         verbose_name_plural=verbose_name
     def __str__(self):
         return self.ip


class DayNumber(models.Model):
    day=models.DateField(verbose_name='日期',default=timezone.now)
    count=models.IntegerField(verbose_name='访问量',default=0)

    class Meta:
        verbose_name='单日访问量'
        verbose_name_plural=verbose_name
    def __str__(self):
        return  str(self.day)


