# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20161013_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Category_text',
            new_name='category_text',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='category',
            name='choice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='person.Choice'),
        ),
    ]
