# Generated by Django 3.1 on 2020-11-07 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20201107_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newtaskform',
            old_name='name',
            new_name='task',
        ),
    ]
