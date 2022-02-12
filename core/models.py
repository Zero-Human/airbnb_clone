from abc import abstractmethod
from turtle import update
from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """Time Stamped Model"""

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # DB에 안 들어가기 위해서 사용 추상화(Django에서 사용)
