# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=post.models.upload_loc, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User')),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
