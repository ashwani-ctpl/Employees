# Generated by Django 2.0.6 on 2018-07-24 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_auto_20180724_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeofficial',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.EmployeeOfficial'),
        ),
        migrations.AlterField(
            model_name='employeeofficial',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]