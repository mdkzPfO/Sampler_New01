# Generated by Django 3.2.12 on 2022-04-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp1app', '0002_auto_20220409_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplingmodel',
            name='animal',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
