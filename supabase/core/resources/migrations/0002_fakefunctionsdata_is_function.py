# Generated by Django 4.2.5 on 2023-09-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakefunctionsdata',
            name='is_function',
            field=models.BooleanField(default=True),
        ),
    ]
