from django.db import models

# Create your models here.
class user_info (models.Model):
    user_name = models.CharField(max_length=32)
    pass_word = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    id = models.AutoField(primary_key = True)