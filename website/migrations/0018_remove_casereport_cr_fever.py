# Generated by Django 4.1.3 on 2022-11-04 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0017_casereport_cr_familyworkspublicexposedplaces_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="casereport", name="CR_Fever",),
    ]
