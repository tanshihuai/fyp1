# Generated by Django 4.0.4 on 2022-08-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_patient_p_email_alter_patient_p_nric_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_RoleName', models.CharField(max_length=20)),
            ],
        ),
    ]