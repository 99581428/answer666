import re
import urllib
from urllib.parse import unquote

from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.shortcuts import HttpResponse
from functools import wraps
# Create your views here.
from cmdb import models
from cmdb.formcheck import FormCheck, FM
from django.contrib import messages

from cmdb.models import user_info
from cmdb.myTools import myTools


def register(request):
    if request.method == "POST":
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        # 调用form_obj校验数据的方法
        if FormCheck.regCheck(request):
            username = request.POST.get("username", None)
            pwd = request.POST.get("pwd", None)
            _phone = request.POST.get("phone", None)
            models.user_info.objects.create(user_name=username, pass_word=pwd, phone=_phone)
            # messages.success(request, "注册成功")
            return render(request, "pagejump.html", {'jumptype':"1"})
    return render(request, "register.html",)

def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        #else:
            #return redirect(reverse('login'))
    return inner

def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method=="POST":
        obj = FM(request.POST)
        if obj.is_valid():

            obj.cleaned_data['pass_word'] = myTools.encryption(obj.cleaned_data['pass_word'])
            print(obj.cleaned_data)
            check_dic = models.user_info.objects.filter(**obj.cleaned_data).first()
            if check_dic is None:
                return render(request, 'login.html',{'errors': "用户名或密码错误"})
            else:
                request.session['user_id'] = check_dic.id
                request.session['user_name'] = check_dic.user_name
                request.session['is_login'] = True
                return redirect(reverse('index'))
        else:
            return render(request, 'login.html', {'errors': "用户名或密码错误"})
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request,'login.html', {'errors': ""})
#注销当前用户
def logout(request):
    del request.session["user_name"]  # 删除session
    del request.session["user_id"]
    request.session['is_login'] = False
    return redirect(reverse('index'))

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
searchdic = None#搜索结果字典
def search(request):
    global searchdic
    if  request.GET.get("key", None) is None:
        searchkey = None
    else:
        searchkey =  unquote(request.GET.get("key", None))
        searchdic = models.knowlageinfo.objects.filter(kname__contains=searchkey).values('kid', 'kname').order_by('kid');
    page = request.GET.get('page')
    fromtype = request.GET.get('fromtype',None)
    _paginator = Paginator(searchdic,10,3)
    try:
        curpagelist = _paginator.page(page)
    except PageNotAnInteger:
        curpagelist = _paginator.page(1)
    except EmptyPage:
        curpagelist = _paginator.page(_paginator.num_pages)
    # if fromtype == "index" :
    #     return redirect(reverse('search'))
    return render(request, 'search.html',{'results':curpagelist})
#@check_login
def answer(request):
    kid = request.GET.get('kid')
    _type= request.Get.get('type')
    if _type is not None:#获取答案
        aswer_detail = models.knowlageinfo.objects.filter(kid=kid).values('kanwers').first()
        aswer_money = 10
        if request.session['is_login']:#判断用户是否登录
            _user_info = models.user_info.objects.filter(id = request.session["user_id"] ).first()#获取用户点券数量
            if _user_info.userright>20: # 20为普通用户，以上全部包含查题vip权限
                return render(request, 'anwer.htnl', locals())
            else :#普通用户扣点券
                sypoint = _user_info.userpoint - aswer_money
                if sypoint>=0 :#判断用户是否有足够的点券
                    models.user_info.objects.filter(id=request.session["user_id"]).update(userpoint = sypoint)
                    return render(request, 'anwer.htnl', locals())
                else :
                    #点券不足，提醒用户充值
                    return render(request, 'anwer.htnl', locals())

                return render(request, 'anwer.htnl', locals())
        else : #返回界面，请用户登录
            return render(request, 'anwer.htnl', locals())
        return render(request,'anwer.htnl',locals())
def index(request):
       # username1=request.session.get('username')
    # user_id1=request.session.get('user_id')

    return render(request,'index.html')





