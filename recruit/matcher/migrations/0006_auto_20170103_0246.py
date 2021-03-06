# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 02:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0005_auto_20170103_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.Person'),
        ),
        migrations.AlterField(
            model_name='match',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matcher.Position'),
        ),
    ]
