#-*- coding:utf-8 -*-
#author:centyuan
#@time:18-11-20 上午10:59
from django.utils.deprecation import MiddlewareMixin
from blogs.models import UseripNum,DayNumber
from django.utils import timezone

class ip_record(MiddlewareMixin):
    def process_request(self,request):

        if 'HTTP_X_FORWARDED_FOR'in request.META:
            client_ip=request.META['HTTP_X_FORWARDED_FOR']
            client_ip=client_ip.split(',')[0]
        else:
            client_ip=request.META['REMOTE_ADDR']
        exist_ip=UseripNum.objects.get(ip=str(client_ip))
        # ip_exist=UseripNum.objects.filter(ip=str(client_ip))
        if exist_ip:
            # num_obj=ip_exist[0]
            # num_obj.numbers +=1
            exist_ip.numbers +=1
            exist_ip.save()
        else:
            num_obj=UseripNum()
            num_obj.ip=client_ip
            num_obj=1
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
