# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_ipmanage_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipmanage',
            name='port',
            field=models.CharField(default='', max_length=50),
        ),
    ]
