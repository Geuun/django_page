from django.db import models

class User(models.Model):
    user_id = models.charField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pw = models.charField(max_length=128, verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16, unique=True, verbose_name='유저 이름')
    user