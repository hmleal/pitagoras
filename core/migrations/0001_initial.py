# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gmm',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('approved_symbol', models.CharField(max_length=75, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'GMM',
                'verbose_name_plural': 'GMM',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PathWay',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('acronym', models.CharField(max_length=75, blank=True)),
                ('type', models.CharField(max_length=75, choices=[('apoptosis', 'Apoptosis')])),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('gmms', models.ManyToManyField(to='core.Gmm')),
            ],
            options={
                'verbose_name': 'Pathway',
                'verbose_name_plural': 'Pathways',
            },
            bases=(models.Model,),
        ),
    ]
