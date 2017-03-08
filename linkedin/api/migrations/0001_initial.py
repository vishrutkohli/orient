# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=1000)),
                ('headline', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=10000)),
                ('summary', models.CharField(max_length=1000)),
                ('specialties', models.CharField(max_length=1000)),
                ('position', models.CharField(max_length=250)),
                ('picture_url', models.CharField(max_length=250)),
                ('public_profile_url', models.CharField(max_length=11250)),
                ('email_address', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saved_id', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idn', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='saved',
            name='idx',
            field=models.ForeignKey(to='api.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='data',
            name='idm',
            field=models.ForeignKey(to='api.Users'),
            preserve_default=True,
        ),
    ]
