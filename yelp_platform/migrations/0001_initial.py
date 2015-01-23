# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_name', models.CharField(max_length=254)),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(max_length=254)),
                ('address3', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=254)),
                ('postal_code', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=254)),
                ('yelp_business_id', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
