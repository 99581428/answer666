import hashlib

from django.db import models

# Create your models here.
from django.utils import timezone

from cmdb.myTools import myTools


class user_info (models.Model):
    user_name = models.CharField(max_length=20,null=False)
    pass_word = models.CharField(max_length=32,null=False)
    phone = models.CharField(max_length=20)
    id = models.AutoField(primary_key = True)
    userright = models.IntegerField()
    userpoint = models.IntegerField(default=0);

    def save(self, *args, **kwargs):
        # 存在就更新，不存在就创建
        self.pass_word = myTools.encryption(self.pass_word)
        super(user_info, self).save(*args, **kwargs)

#题库表
class knowlageinfo (models.Model):
    kid = models.AutoField(primary_key = True)
    kname = models.CharField(max_length=1000,null=False)
    kanwers = models.CharField(max_length=1000)#答案
    kanwersid = models.IntegerField()#答题者id
    ktype1 = models.IntegerField()#所属科目
    ktype2 = models.IntegerField()#所属试卷或课件
    ktype3 = models.IntegerField()#题目类型

#科目列表
class kmtype (models.Model):
    kid = models.AutoField(primary_key = True)
    kname = models.CharField(max_length=32,null=False)
#课件列表
class kjtype (models.Model):
    kid= models.AutoField(primary_key = True)
    kname = models.CharField(max_length=32,null=False)
#我要答题
class answerques (models.Model):
    id = models.AutoField(primary_key = True)
    kid = models.IntegerField()
    kanwers = models.CharField(max_length=2000)  # 答案
    kanwersid = models.IntegerField()
    ksubdate = models.DateTimeField('保存日期',default = timezone.now)


