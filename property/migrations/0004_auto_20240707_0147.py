# Generated by Django 3.2.10 on 2024-07-06 22:47

from django.db import migrations


def define_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20240707_0145'),
    ]

    operations = [
        migrations.RunPython(define_new_building)
    ]
