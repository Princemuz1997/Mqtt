# Generated by Django 2.2.7 on 2020-09-07 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor',
            new_name='Device',
        ),
    ]
