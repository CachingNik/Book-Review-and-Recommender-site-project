# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-29 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_added_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_by_user',
            field=models.CharField(max_length=30),
        ),
    ]