# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('uuid', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('request_time', models.DateTimeField()),
                ('product_id', models.CharField(max_length=254, null=True)),
                ('status', models.CharField(max_length=254)),
                ('distance', models.FloatField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('uber_uuid', models.CharField(max_length=254, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ride',
            name='user',
            field=models.ForeignKey(to='uber.User'),
            preserve_default=True,
        ),
    ]
