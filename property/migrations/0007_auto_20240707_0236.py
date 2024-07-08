# Generated by Django 3.2.10 on 2024-07-06 23:36

from django.db import migrations
from phonenumbers import parse


def parse_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for obj in list(Flat.objects.all()):
        obj.owner_pure_phone = parse(obj.owners_phonenumber, 'RU')
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_rename_phonenumber_flat_owner_pure_phone'),
    ]

    operations = [
    ]