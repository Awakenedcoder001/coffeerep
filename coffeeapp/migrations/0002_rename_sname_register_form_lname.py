# Generated by Django 4.0 on 2021-12-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_form',
            old_name='sname',
            new_name='lname',
        ),
    ]
