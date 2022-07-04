# Generated by Django 3.2.12 on 2022-06-13 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Original_GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_group', models.CharField(max_length=100, null=True)),
                ('slave_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SamplingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, null=True)),
                ('animal', models.CharField(default=None, max_length=100, null=True)),
                ('purpose', models.CharField(default=None, max_length=100, null=True)),
                ('method', models.CharField(default=None, max_length=100, null=True)),
                ('group_name01', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number01', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation01', models.CharField(default=None, max_length=100, null=True)),
                ('group_name02', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number02', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation02', models.CharField(default=None, max_length=100, null=True)),
                ('group_name03', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number03', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation03', models.CharField(default=None, max_length=100, null=True)),
                ('group_name04', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number04', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation04', models.CharField(default=None, max_length=100, null=True)),
                ('group_name05', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number05', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation05', models.CharField(default=None, max_length=100, null=True)),
                ('group_name06', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_number06', models.CharField(default=None, max_length=100, null=True)),
                ('experiment_situation06', models.CharField(default=None, max_length=100, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='img/')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('origin_groups', models.ManyToManyField(to='exp1app.Original_GroupModel')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(null=True)),
                ('suggestion', models.TextField(null=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=100, null=True)),
                ('animal_purpose', models.TextField(null=True)),
                ('manager', models.TextField(null=True)),
                ('wash', models.TextField(null=True)),
                ('wash_frequency', models.TextField(null=True)),
                ('feed', models.TextField(null=True)),
                ('feed_frequency', models.TextField(null=True)),
                ('temprature', models.TextField(null=True)),
                ('location', models.TextField(null=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
