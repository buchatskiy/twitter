# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 24, 13, 51, 19, 624000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
