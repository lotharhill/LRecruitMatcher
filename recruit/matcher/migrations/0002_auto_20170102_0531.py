# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='current_employer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='matcher.Company'),
        ),
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='matcher.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='contact_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='matcher.Person'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]