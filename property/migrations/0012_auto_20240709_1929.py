# Generated by Django 3.2.10 on 2024-07-09 16:29

from django.db import migrations


def connect_owner_and_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for obj in list(Flat.objects.all()):
        Owner.objects.get_or_create(flats=obj.id,
                                    )
        Owner.objects.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20240708_1755'),
    ]

    operations = [
        migrations.RunPython(connect_owner_and_flat)
    ]
