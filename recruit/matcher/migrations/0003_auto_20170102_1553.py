# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0002_auto_20170102_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='current_employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.Company'),
        ),
        migrations.AlterField(
            model_name='position',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.Company'),
        ),
    ]
