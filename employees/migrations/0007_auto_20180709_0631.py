# Generated by Django 2.0.6 on 2018-07-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20180706_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
