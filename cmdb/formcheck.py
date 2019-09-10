import re

from django import forms


class FormCheck():
    def regCheck(request):
        username = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        pwd2 = request.POST.get("pwd2", None)
        _phone = request.POST.get("phone", None)
        dtm = request.POST.get("dtm", None)
        if(len(username.strip())<=0):
            return False
        username_re = re.compile(r'^[a-zA-Z][a-zA-Z0-9]{6,20}$')
        if not username_re.match(username):
            return False
        if(len(pwd)<8 or len(pwd)>16 or (pwd!=pwd2)):
            return False
        return True
class FM(forms.Form):
    #这里要接受后端需要的，不需要的数据不会关注
    user_name=forms.CharField(error_messages={'required':"不能为空"})  #表单中的name要与变量名一样
    pass_word=forms.CharField(
        min_length=8,
        error_messages={'required':"不能为空",
                        'min_length':'密码长度不小于8',},
    )


