# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django_enumfield.db.fields
import yunity.conversations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', django_enumfield.db.fields.EnumField(default=0, enum=yunity.conversations.models.ConversationType)),
                ('topic', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
