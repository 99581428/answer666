from  django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    user_name = forms.CharField(error_messages={'required': "不能为空"})  # 表单中的name要与变量名一样
    pass_word = forms.CharField(
        min_length=8,
        error_messages={'required': "不能为空",
                        'min_length': '密码长度不小于8', },)
    captcha = CaptchaField()
class CaptchaForm(forms.Form):
    captcha = CaptchaField()