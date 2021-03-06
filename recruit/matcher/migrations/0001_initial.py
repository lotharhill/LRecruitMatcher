# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('main_number', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('zip_code', models.IntegerField(max_length=9)),
                ('description', models.TextField(max_length=1000)),
                ('industry', models.TextField(max_length=100)),
                ('size', models.CharField(max_length=30)),
                ('website', models.URLField()),
                ('linkedin_profile', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('salary', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('title', models.TextField(max_length=100)),
                ('suffix', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('linkedin_profile', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('position_zip', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('position_id', models.IntegerField()),
                ('title_code', models.CharField(max_length=30)),
                ('city', models.TextField(max_length=100)),
                ('salary_lower', models.IntegerField()),
                ('salary_upper', models.IntegerField()),
                ('job_description', models.TextField(max_length=10000)),
                ('telephone_count', models.IntegerField()),
                ('in_person_count', models.IntegerField()),
                ('notes', models.TextField(max_length=1000)),
                ('presentation_count', models.IntegerField()),
                ('benefits', models.TextField(max_length=100)),
                ('social_linkedin', models.URLField()),
                ('resume_count', models.IntegerField()),
                ('offer_made_count', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
