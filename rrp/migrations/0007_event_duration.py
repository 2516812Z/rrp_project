# Generated by Django 2.1.5 on 2022-08-16 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrp', '0006_auto_20220816_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]
