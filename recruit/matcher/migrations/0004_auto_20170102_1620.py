# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0003_auto_20170102_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='in_person_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='offer_made_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_zip',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='presentation_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='resume_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary_lower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='salary_upper',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='position',
            name='telephone_count',
            field=models.IntegerField(default=0),
        ),
    ]
