# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-13 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_is_share_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_share_post',
        ),
        migrations.AddField(
            model_name='post',
            name='reason_share',
            field=models.CharField(default='share', max_length=10),
            preserve_default=False,
        ),
    ]
