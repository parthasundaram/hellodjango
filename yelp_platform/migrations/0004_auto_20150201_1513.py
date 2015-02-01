# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yelp_platform', '0003_auto_20150131_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='id',
        ),
        migrations.AddField(
            model_name='business',
            name='partner_business_id',
            field=models.CharField(default='123', max_length=254, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
