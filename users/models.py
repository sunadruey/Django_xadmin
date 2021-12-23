from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=300)

    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

AUTH_USER_MODEL = 'users.User'