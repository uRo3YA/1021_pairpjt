# Generated by Django 3.2.13 on 2022-10-21 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221021_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='review',
        ),
    ]
