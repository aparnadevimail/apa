# Generated by Django 4.1.6 on 2023-03-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-07-21'),
            preserve_default=False,
        ),
    ]
