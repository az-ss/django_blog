# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=30)),
                ('content', models.TextField()),
                ('user_name', models.TextField(max_length=30)),
            ],
        ),
    ]
