# Generated by Django 5.0.6 on 2024-10-23 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_hospital_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Hospital_name',
            new_name='hospital_name',
        ),
    ]
