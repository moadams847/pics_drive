# Generated by Django 3.2.8 on 2022-01-04 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0013_deletepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]