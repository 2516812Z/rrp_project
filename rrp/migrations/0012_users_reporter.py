# Generated by Django 2.1.5 on 2022-08-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrp', '0011_auto_20220819_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='reporter',
            field=models.BooleanField(default=False),
        ),
    ]
