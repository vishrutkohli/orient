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
                ('typeof', models.CharField(max_length=100, null=True)),
                ('date', models.CharField(max_length=1000, null=True)),
                ('duration', models.CharField(max_length=10000, null=True)),
                ('severity', models.CharField(max_length=1000, null=True)),
                ('review', models.CharField(default=b'NULL', max_length=1000, null=True)),
                ('medicine', models.CharField(default=b'NULL', max_length=1000, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='data',
            name='uid',
            field=models.ForeignKey(to='main.Users', null=True),
            preserve_default=True,
        ),
    ]
