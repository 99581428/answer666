import re
import urllib
from urllib.parse import unquote

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.shortcuts import HttpResponse
from functools import wraps
# Create your views here.
from django_redis import cache

from cmdb import models
from cmdb.formcheck import FormCheck, FM
from django.contrib import messages

from cmdb.forms import UserForm
from cmdb.models import user_info
from cmdb.myTools import myTools,myHttpReturnData

import logging

from cmdb.sendsmsutils import send_sms, send_sms_view, checkPhoneCode

logger = logging.getLogger('suser')
errors = logging.getLogger('django.request')

def register(request):
    if request.method == "POST":
        logger.info('url:%s method:%s 注册数据' % (request.path, request.method))
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        # 调用form_obj校验数据的方法
        if FormCheck.regCheck(request):
            username = request.POST.get("username", None)
            pwd = request.POST.get("pwd", None)
            _phone = request.POST.get("phone", None)
            models.user_info.objects.create(user_name=username, pass_word=pwd, phone=_phone,userright=20)
            # messages.success(request, "注册成功")
            logger.info('url:%s method:%s 注册成功' % (request.path, request.method))
            return render(request, "pagejump.html", {'jumptype':"1"})
        else:
            return render(request,"register.html",request)
    else:

        return render(request, "register.html")
def ajaxreg(request):
        username = request.POST.get("username", None)
        logger.info('url:%s method:%s 检测用户名' % (request.path, username))
        _list1= models.user_info.objects.filter(user_name=username);
        _list2 =  models.user_info.objects.filter(phone=username);
        if len(_list1)<=0 and len(_list2)<=0 :
            logger.info('url:%s method:%s 检测用户名0' % (request.path, username))
            return HttpResponse("0")
        else :
            logger.info('url:%s method:%s 检测用户名1' % (request.path, username))
            return HttpResponse("1")
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
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['user_name']
            pwd = myTools.encryption(login_form.cleaned_data['pass_word'])
            check_dic = models.user_info.objects.filter(user_name=user_name, pass_word=pwd).first()
            if check_dic is None:
                logger.info('url:%s method:%s 登陆失败' % (request.path, request.method))
                return render(request, 'login.html',{'errors': "用户名或密码错误",'login_form':login_form})
            else:
                request.session['user_id'] = check_dic.id
                request.session['user_name'] = check_dic.user_name
                request.session['is_login'] = True
                logger.info('url:%s method:%s 登陆成功' % (request.path, request.method))
                return redirect(reverse('index'))
        else:
            return render(request, 'login.html', {'errors': "验证码错误",'login_form':login_form})
    else:
        login_form = UserForm();
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request,'login.html', {'errors': "",'login_form':login_form})
#注销当前用户
def logout(request):
    del request.session["user_name"]  # 删除session
    del request.session["user_id"]
    request.session['is_login'] = False
    logger.info('url:%s method:%s 注销用户' % (request.path, request.method))
    return redirect(reverse('index'))

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
searchdic = None#搜索结果字典
def search(request):
    global searchdic
    if  request.GET.get("key", None) is None:
        searchkey = None
        return render(request, 'search.html')
    else:
        logger.info('url:%s method:%s key:%s' % (request.path, request.method,request.GET.get("key")))
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
    if request.method=="GET":
        kid = request.GET.get('id')
        answer_info = models.knowlageinfo.objects.filter(kid=kid).values('kid', 'kname').first()
        return render(request, 'aswer.html', {'answerinfo': answer_info})
    else:
        #获取答案
        kid = request.POST.get('kid')
        aswer_detail = models.knowlageinfo.objects.filter(kid=kid).values('kanwers')
        jsondata = json.dumps(list(aswer_detail), cls=DjangoJSONEncoder)
        aswer_money = 10
        user_id = request.session.get("user_id")
        if user_id is not None:#判断用户是否登录
            _user_info = models.user_info.objects.filter(id = request.session["user_id"] ).first()#获取用户点券数量
            if _user_info.userright>20: # 20为普通用户，以上全部包含查题vip权限
                return HttpResponse(jsondata, content_type="application/json")
            else :#普通用户扣点券
                sypoint = _user_info.userpoint - aswer_money
                if sypoint>=0 :#判断用户是否有足够的点券
                    models.user_info.objects.filter(id=request.session["user_id"]).update(userpoint = sypoint)
                    return HttpResponse(jsondata, content_type="application/json")
                else :
                    #点券不足，提醒用户充值
                    jsondata = json.dumps([{'errors':1}])
                    return HttpResponse(jsondata, content_type="application/json")
        else : #返回界面，请用户登录
            jsondata = json.dumps([{'errors': 2}])
            return HttpResponse(jsondata, content_type="application/json")
def index(request):
       # username1=request.session.get('username')
    # user_id1=request.session.get('user_id')

    return render(request,'index.html')
#提交答案
def myanswers(request):
    if request.method=="GET":
        kid = request.GET.get('id')
        answer_info = models.knowlageinfo.objects.filter(kid=kid).first()
        return render(request,'myanswer.html',locals())
    else:
        kid = request.POST.get('id')
        kanwers = request.POST.get('kanwers')
        kanwersid = request.session.get("user_id")
        if kid and kanwers and kanwersid:
            models.answerques.objects.create(kid=kid, kanwers=kanwers, kanwersid=kanwersid);
            return render(request, "pagejump.html", {'jumptype': "2"})
        else :
            return HttpResponse("数据错误，请检查或联系客服人员")

#个人中心
def myinformation(request):
    if request.method=="GET":
        _id = request.session['user_id']
        if _id:
            userinfo = models.user_info.objects.filter(id=_id).first()
            phone = request.GET.get('phone')
            if request.GET.get('phone'):
                send_sms_view(request)
            return render(request,'myinformation.html',locals())
        else:
            return redirect(reverse('login'))
    else:
        pho = request.POST.get('phone')
        _codp =  request.POST.get('dtm')
        if len(pho)<11:
            return render(request, 'myinformation.html',{'errors':"手机号码输入错误"})
        else:
            if checkPhoneCode(pho,_codp):
                models.user_info.objects.filter(id=request.session["user_id"]).update(phone=pho)
        return render(request, 'myinformation.html')
# 联系我们
def contactus(request):
    return render(request,'contactus.html')







