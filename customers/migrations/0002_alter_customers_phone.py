# Generated by Django 5.0.6 on 2024-06-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
