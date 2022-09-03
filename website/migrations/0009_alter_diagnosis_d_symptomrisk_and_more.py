# Generated by Django 4.0.4 on 2022-08-21 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_casereport_doctorqueue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='D_SymptomRisk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.doctorqueue'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='D_XRayRisk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.xrayqueue'),
        ),
        migrations.AlterField(
            model_name='doctorqueue',
            name='DQ_PatientID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.casereport'),
        ),
        migrations.AlterField(
            model_name='xrayqueue',
            name='XR_PatientID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website.doctorqueue'),
        ),
    ]