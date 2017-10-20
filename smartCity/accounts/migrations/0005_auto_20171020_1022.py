# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171020_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='businessmanInfo',
            new_name='collegesLink',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='studentInfo',
            new_name='hotelsLink',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='touristInfo',
            new_name='industriesLink',
        ),
        migrations.AddField(
            model_name='city',
            name='librariesLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='mallsLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='museumsLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='parksLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='restaurantsLink',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='city',
            name='zoosLink',
            field=models.URLField(default=''),
        ),
    ]