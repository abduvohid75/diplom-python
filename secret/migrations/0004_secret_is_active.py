# Generated by Django 3.2.20 on 2023-11-11 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0003_alter_secret_generated_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
