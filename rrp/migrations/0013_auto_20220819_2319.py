# Generated by Django 2.1.5 on 2022-08-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rrp', '0012_users_reporter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Handler',
            new_name='handler',
        ),
    ]