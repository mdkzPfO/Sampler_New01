# Generated by Django 3.2.12 on 2022-04-03 07:47

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
            name='UseChildrenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Children_Name', models.TextField(default='Guest', null=True)),
                ('Children_Email', models.TextField(default='Guest', null=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SamplingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, null=True)),
                ('animal', models.TextField(default=None, null=True)),
                ('purpose', models.TextField(default=None, null=True)),
                ('method', models.TextField(default=None, null=True)),
                ('control_number', models.TextField(default=None, null=True)),
                ('control_situation', models.TextField(default=None, null=True)),
                ('experiment_number', models.TextField(default=None, null=True)),
                ('experiment_situation', models.TextField(default=None, null=True)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
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
                ('Animal', models.CharField(max_length=100, null=True)),
                ('purpose', models.TextField(null=True)),
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
