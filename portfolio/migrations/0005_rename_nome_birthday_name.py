# Generated by Django 4.2.1 on 2023-06-19 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='birthday',
            old_name='nome',
            new_name='name',
        ),
    ]
