# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0035_auto_20170529_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparkjobrunalert',
            name='temp_id',
            field=models.IntegerField(null=True),
        ),
    ]
