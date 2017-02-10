# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='email_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='headline',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='idm',
            field=models.ForeignKey(to='api.Users', null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='last_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='location',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='mac_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='picture_url',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='position',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='public_profile_url',
            field=models.CharField(max_length=11250, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='specialties',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='summary',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
