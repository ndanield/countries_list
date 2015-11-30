# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=46)),
                ('continent', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=30)),
                ('population', models.IntegerField()),
            ],
        ),
    ]
