# Generated by Django 4.0.4 on 2022-08-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='P_Name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Phone',
            new_name='P_Phone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='NRIC',
        ),
        migrations.AddField(
            model_name='patient',
            name='P_Email',
            field=models.EmailField(default='patient@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='P_NRIC',
            field=models.CharField(default=1, max_length=9, unique=True),
            preserve_default=False,
        ),
    ]