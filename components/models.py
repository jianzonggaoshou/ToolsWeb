from django.db import models
from django.contrib.auth.models import User


class Chasis(models.Model):
    height = models.CharField(max_length=32)
    wide = models.CharField(max_length=32)


class Component(models.Model):
    """
    部件
    """
    name = models.CharField(unique=True, max_length=32, verbose_name='名称')
    chasis = models.OneToOneField(Chasis, null=True, blank=True, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='提交人')

