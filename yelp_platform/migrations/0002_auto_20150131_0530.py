# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_platform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address2',
            field=models.CharField(max_length=254, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='business',
            name='address3',
            field=models.CharField(max_length=254, null=True),
            preserve_default=True,
        ),
    ]
