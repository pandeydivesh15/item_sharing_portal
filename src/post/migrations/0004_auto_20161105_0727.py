# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-05 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=120),
        ),
    ]