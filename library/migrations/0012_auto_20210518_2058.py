# Generated by Django 3.1.2 on 2021-05-18 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20210518_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]