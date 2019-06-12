from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    """
    部件
    """
    name = models.CharField(unique=True, max_length=32, verbose_name='名称')
    submitter = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='提交人')

