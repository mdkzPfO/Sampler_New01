# Generated by Django 3.2.12 on 2022-06-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp1app', '0002_remove_samplingmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='samplingmodel',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='img/'),
        ),
    ]
