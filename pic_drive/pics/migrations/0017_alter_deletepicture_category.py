# Generated by Django 3.2.8 on 2022-01-06 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0016_alter_deletedfolder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deletepicture',
            name='category',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.CASCADE, to='pics.deletedfolder'),
        ),
    ]
