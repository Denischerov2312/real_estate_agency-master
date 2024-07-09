# Generated by Django 3.2.10 on 2024-07-08 14:55

from django.db import migrations


def parse_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for obj in list(Flat.objects.all()):
        Owner.objects.get_or_create(name=obj.owner,
                                    phonenumber=obj.owners_phonenumber,
                                    pure_phonenumber=obj.owner_pure_phone,
                                    )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(parse_phonenumber)
    ]
