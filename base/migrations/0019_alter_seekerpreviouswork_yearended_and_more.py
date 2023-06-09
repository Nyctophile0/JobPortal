# Generated by Django 4.0.1 on 2022-02-06 17:16

import base.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_seekerpreviouswork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerpreviouswork',
            name='yearEnded',
            field=models.PositiveIntegerField(default=2022, validators=[django.core.validators.MinValueValidator(1984), base.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='seekerpreviouswork',
            name='yearStarted',
            field=models.PositiveIntegerField(default=2022, validators=[django.core.validators.MinValueValidator(1984), base.models.max_value_current_year]),
        ),
    ]