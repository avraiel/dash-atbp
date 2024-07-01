# Generated by Django 5.0.6 on 2024-06-30 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='snippets.role'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='deleted_on',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
