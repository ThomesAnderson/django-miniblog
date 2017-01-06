# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=2000)),
            ],
        ),
    ]