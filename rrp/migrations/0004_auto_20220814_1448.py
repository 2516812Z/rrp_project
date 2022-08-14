# Generated by Django 2.1.5 on 2022-08-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrp', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='assetType',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='currentProcess',
            field=models.CharField(default='C&A', max_length=30),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='evidence',
            field=models.ImageField(blank=True, upload_to='evidence'),
        ),
        migrations.AddField(
            model_name='event',
            name='isKnown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='ransomAmount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='ransomwareName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='ransomwareType',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='records',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='recoveryInfo',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='recoveryTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='recoveryType',
            field=models.CharField(default='Non', max_length=30),
        ),
        migrations.AddField(
            model_name='event',
            name='reporters',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='requestTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='riskLevel',
            field=models.CharField(default='L1', max_length=30),
        ),
    ]
