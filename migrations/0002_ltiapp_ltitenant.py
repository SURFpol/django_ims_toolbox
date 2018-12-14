# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-05 12:44
from __future__ import unicode_literals

import datagrowth.configuration.fields
from django.db import migrations, models
import django.db.models.deletion
import oauthlib.common
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LTIApp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('view', models.CharField(choices=[('share:common-cartridge-upload', 'Common Cartridge upload'), ('share:common-cartridge-fetch', 'Common Cartridge fetch')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('privacy_level', models.CharField(choices=[('anonymous', 'anonymous'), ('email_only', 'email_only'), ('name_only', 'name_only'), ('public', 'public')], max_length=50)),
            ],
            options={
                'verbose_name': 'LTI app',
                'verbose_name_plural': 'LTI apps',
            },
        ),
        migrations.CreateModel(
            name='LTITenant',
            fields=[
                ('organization', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('lms', models.CharField(choices=[('canvas', 'canvas'), ('moodle', 'moodle')], max_length=256)),
                ('config', datagrowth.configuration.fields.ConfigurationField(blank=True, default={})),
                ('client_key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='consumer key')),
                ('client_secret', models.CharField(default=oauthlib.common.generate_token, editable=False, max_length=30, verbose_name='shared secret')),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('api_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.LTIApp')),
            ],
            options={
                'verbose_name': 'LTI tenant',
                'verbose_name_plural': 'LTI tenant',
            },
        ),
    ]