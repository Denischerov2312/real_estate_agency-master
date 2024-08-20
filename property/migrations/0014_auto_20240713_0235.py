# Generated by Django 3.2.10 on 2024-07-12 23:35

from django.db import migrations


def connect_owner_and_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for obj in list(Flat.objects.all()):
        Owner.objects.get(phonenumber=obj.phonenumber)
        break


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_owner_pure_phonenumber'),
    ]

    operations = [
        migrations.RunPython(connect_owner_and_flat)
    ]