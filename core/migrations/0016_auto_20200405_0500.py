# Generated by Django 3.0.5 on 2020-04-04 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200405_0459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='item',
        ),
    ]