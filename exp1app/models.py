# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
EVALUATION_CHOICES=[('良い','良い'),('悪い','悪い')]
#サンプリングのデータベース
class SamplingModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    animal=models.TextField(null=True)
    purpose=models.TextField(null=True)
    method=models.TextField(null=True)
    control_number=models.TextField(null=True)
    control_situation=models.TextField(null=True)
    experiment_number=models.TextField(null=True)
    experiment_situation=models.TextField(null=True)
#毎日のレポートのデータベース
class ReportModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    status=models.TextField(null=True)
    suggestion=models.TextField(null=True)
#動物のデータベース
class AnimalModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Animal=models.CharField(max_length=100,null=True)
    purpose=models.TextField(null=True)
    manager=models.TextField(null=True)
    wash=models.TextField(null=True)
    wash_frequency=models.TextField(null=True)
    feed=models.TextField(null=True)
    feed_frequency=models.TextField(null=True)
    temprature=models.TextField(null=True)
    location=models.TextField(null=True)
