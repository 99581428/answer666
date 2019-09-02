from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from cmdb import models


def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        pwd = request.POST.get("pwd",None)
        _phone = request.POST.get("phone",None)
        print(username +"-"+pwd+"-"+_phone)
        models.user_info.objects.create(user_name=username, pass_word=pwd, phone=_phone)


    return render(request,"index.html",)