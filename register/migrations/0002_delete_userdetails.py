# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetails',
        ),
    ]
