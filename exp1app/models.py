# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
EVALUATION_CHOICES=[('良い','良い'),('悪い','悪い')]
#サンプリングのデータベース
class SamplingModel(models.Model):
    title=models.CharField(max_length=100,null=True,default=None)
    animal=models.CharField(max_length=100,null=True,default=None)
    purpose=models.CharField(max_length=100,null=True,default=None)
    control_number=models.CharField(max_length=100,null=True,default=None)
    method=models.CharField(max_length=100,null=True,default=None)
    control_situation=models.CharField(max_length=100,null=True,default=None)
    experiment_number=models.CharField(max_length=100,null=True,default=None)
    experiment_situation=models.CharField(max_length=100,null=True,default=None)
    datetime = models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
#毎日のレポートのデータベース
class ReportModel(models.Model):
    status=models.TextField(null=True)
    suggestion=models.TextField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
#動物のデータベース
class AnimalModel(models.Model):
    animal=models.CharField(max_length=100,null=True)
    animal_purpose=models.TextField(null=True)
    manager=models.TextField(null=True)
    wash=models.TextField(null=True)
    wash_frequency=models.TextField(null=True)
    feed=models.TextField(null=True)
    feed_frequency=models.TextField(null=True)
    temprature=models.TextField(null=True)
    location=models.TextField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
class UseChildrenModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    Children_Name=models.TextField(null=True,default="Guest")
    Children_Email=models.TextField(null=True,default="Guest")
