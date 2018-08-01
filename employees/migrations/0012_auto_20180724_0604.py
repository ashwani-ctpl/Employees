# Generated by Django 2.0.6 on 2018-07-24 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_auto_20180723_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-')], default=None, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='employeeofficial',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employeeofficial',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
