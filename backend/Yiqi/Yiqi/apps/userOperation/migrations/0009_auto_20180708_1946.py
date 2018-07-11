# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userOperation', '0008_auto_20180708_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browseusermodel',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_db', to='activity.ActivityModel', verbose_name='浏览活动'),
        ),
    ]