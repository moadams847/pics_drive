# Generated by Django 3.2.8 on 2022-01-04 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0010_deletepicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deletepicture',
            old_name='date_posted',
            new_name='date_deleted',
        ),
    ]
