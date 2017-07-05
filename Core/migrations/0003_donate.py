# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20170702_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
                ('email', models.CharField(max_length=999)),
                ('comment', models.TextField()),
                ('transactionId', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
