# Generated by Django 5.0.3 on 2024-03-11 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0012_applyforleave_reject_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyforleave',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
