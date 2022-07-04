# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
EVALUATION_CHOICES=[('良い','良い'),('悪い','悪い')]
#サンプリングのデータベース
class Original_GroupModel(models.Model):
    origin_group=models.CharField(max_length=100,null=True)
    slave_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
class SamplingModel(models.Model):
    title=models.CharField(max_length=100,null=True,default=None)
    animal=models.CharField(max_length=100,null=True,default=None)
    purpose=models.CharField(max_length=100,null=True,default=None)
    method=models.CharField(max_length=100,null=True,default=None)
    group_name01=models.CharField(max_length=100,null=True,default=None)
    experiment_number01=models.CharField(max_length=100,null=True,default=None)
    experiment_situation01=models.CharField(max_length=100,null=True,default=None)
    group_name02=models.CharField(max_length=100,null=True,default=None)
    experiment_number02=models.CharField(max_length=100,null=True,default=None)
    experiment_situation02=models.CharField(max_length=100,null=True,default=None)
    group_name03=models.CharField(max_length=100,null=True,default=None)
    experiment_number03=models.CharField(max_length=100,null=True,default=None)
    experiment_situation03=models.CharField(max_length=100,null=True,default=None)
    group_name04=models.CharField(max_length=100,null=True,default=None)
    experiment_number04=models.CharField(max_length=100,null=True,default=None)
    experiment_situation04=models.CharField(max_length=100,null=True,default=None)
    group_name05=models.CharField(max_length=100,null=True,default=None)
    experiment_number05=models.CharField(max_length=100,null=True,default=None)
    experiment_situation05=models.CharField(max_length=100,null=True,default=None)
    group_name06=models.CharField(max_length=100,null=True,default=None)
    experiment_number06=models.CharField(max_length=100,null=True,default=None)
    experiment_situation06=models.CharField(max_length=100,null=True,default=None)
    image = models.ImageField(upload_to='img/',default=None,null=True)
    datetime = models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,default=None)
    origin_groups=models.ManyToManyField(Original_GroupModel)
    def __str__(self):
        return self.title
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
