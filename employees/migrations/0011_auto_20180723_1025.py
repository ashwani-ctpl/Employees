# Generated by Django 2.0.6 on 2018-07-23 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0010_auto_20180723_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeofficial',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
