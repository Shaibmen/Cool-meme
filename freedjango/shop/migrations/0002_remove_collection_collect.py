# Generated by Django 5.2 on 2025-04-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='collect',
        ),
    ]
