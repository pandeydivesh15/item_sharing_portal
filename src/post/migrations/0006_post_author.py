# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-06 14:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('post', '0005_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='User.User'),
            preserve_default=False,
        ),
    ]
