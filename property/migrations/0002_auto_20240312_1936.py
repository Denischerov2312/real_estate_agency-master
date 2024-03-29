# Generated by Django 3.2.10 on 2024-03-12 16:36

from django.db import migrations


def define_is_new_building(apps, shcema_editor):
    flat = apps.get_model('property', 'Flat')
    for obj in list(flat.objects.all()):
        if obj.construction_year >= 2015:
            obj.new_building = True
        else:
            obj.new_building = False
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(define_is_new_building)
    ]
