# Generated by Django 5.0 on 2025-01-05 01:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.UUIDField(default=uuid.UUID('bb893cce-5c50-4830-a46e-53f1fd3af88b'), primary_key=True, serialize=False, unique=True),
        ),
    ]
