from django.shortcuts import render,reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect


from utils.email_send import send_register_email


from .models import UserProfile,EmailVerifyRecord
from .forms import LoginForm,RegisterForm
#自定义auth认证类
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user= UserProfile.objects.get(Q(username=username)|Q(email=username))
            #Q(username=username)|Q(email=username)或用户邮箱都可以登录
            if user.check_password(password):#检查密码
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():#如果验证成功
            user_name=request.POST.get("username")
            pass_word=request.POST.get("password")
            user=authenticate(username=user_name,password=pass_word)#验证密码用户
            if user is not None:
                #if user.is_active:
                login(request,user)#根据用户信息生成一个session
                #return render(request,"index.html")
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})

        else:
            return render(request,"login.html",{"login_form":login_form})

class Register(View):
    def get(self,request):
        register_form=RegisterForm()
        return render(request,"register.html",{"register_form":register_form})

    def post(self,request):
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user_name=request.POST.get("email")
            if UserProfile.objects.filter(email=user_name):
                return  render(request,'register.html',{"msg":"用户已经被注册"})
            pass_word=request.POST.get("password")
            user_profile=UserProfile()#实例
            user_profile.username=user_name
            user_profile.email=user_name
            user_profile.is_active=False #用户激活
            user_profile.password=make_password(pass_word)
            #make_password(pass_word)对密码明文进行加密
            user_profile.save()
            send_register_email(user_name,"register")#发送邮件
            #return render(request,'login.html')
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request,'register.html',{"register_form":register_form})

class ActiveUserView(View):
    def get(self,request,active_code):
        all_records=EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email=record.email
                user=UserProfile.objects.get(email=email)
                user.is_active=True
                user.save()
        #return render(request,'login.html')
        return  HttpResponseRedirect(reverse('login'))

