# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
