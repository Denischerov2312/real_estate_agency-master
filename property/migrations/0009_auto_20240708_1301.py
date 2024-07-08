# Generated by Django 3.2.10 on 2024-07-08 10:01

from django.db import migrations
from phonenumbers import parse
from phonenumbers import is_valid_number


def parse_phonenumber(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for obj in list(Flat.objects.filter(owners_phonenumber='+70000000000')):
        num = parse(obj.owners_phonenumber, 'RU')
        if is_valid_number(num):
            obj.owner_pure_phone = num
        else:
            obj.owner_pure_phone = None
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20240708_0212'),
    ]

    operations = [
        migrations.RunPython(parse_phonenumber)
    ]
