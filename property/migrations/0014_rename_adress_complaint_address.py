# Generated by Django 3.2.24 on 2024-10-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20241001_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='adress',
            new_name='address',
        ),
    ]
