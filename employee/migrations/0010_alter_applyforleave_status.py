# Generated by Django 5.0.2 on 2024-03-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_applyforleave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyforleave',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Rejected')], default=0),
        ),
    ]
