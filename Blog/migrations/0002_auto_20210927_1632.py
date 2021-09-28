# Generated by Django 3.2.7 on 2021-09-27 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodels',
            name='date',
        ),
        migrations.AddField(
            model_name='blogmodels',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodels',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
