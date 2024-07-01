# Generated by Django 5.0.6 on 2024-06-30 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_employee_role_alter_role_deleted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='added_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.employee'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='ended_on',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]