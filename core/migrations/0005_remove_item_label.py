# Generated by Django 3.0.5 on 2020-04-04 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]