# Generated by Django 5.0.3 on 2024-04-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_remove_employee_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applyforleave',
            name='reason',
        ),
        migrations.AddField(
            model_name='applyforleave',
            name='leave_entries',
            field=models.CharField(choices=[('Full Leave', 'Full Leave'), ('Half Leave', 'Half Leave')], default='Full Leave', max_length=20),
        ),
        migrations.AlterField(
            model_name='applyforleave',
            name='days',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]