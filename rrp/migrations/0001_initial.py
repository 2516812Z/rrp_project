# Generated by Django 2.1.5 on 2022-08-21 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('assetName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('assetType', models.CharField(max_length=30, null=True)),
                ('dataLevel', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requestTime', models.DateTimeField(null=True)),
                ('ransomwareName', models.CharField(max_length=30, null=True)),
                ('ransomwareType', models.CharField(max_length=30, null=True)),
                ('ransomAmount', models.IntegerField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('riskLevel', models.CharField(default='L1', max_length=30)),
                ('isKnown', models.BooleanField(default=False)),
                ('recoveryType', models.CharField(default='Non', max_length=30)),
                ('recoveryTime', models.IntegerField(null=True)),
                ('recoveryInfo', models.TextField(max_length=500, null=True)),
                ('handler', models.CharField(max_length=30, null=True)),
                ('records', models.TextField(max_length=500, null=True)),
                ('currentProcess', models.CharField(default='C&A', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('picURL', models.ImageField(blank=True, upload_to='evidence_images')),
                ('eventId', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='rrp.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, null=True)),
                ('info', models.TextField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ransomware',
            fields=[
                ('ransomwareName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('ransomwareType', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskLevelAssessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dataLevel', models.CharField(max_length=30)),
                ('ransomwareType', models.CharField(max_length=30, null=True)),
                ('riskLevel', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('position', models.CharField(max_length=30, null=True)),
                ('superior', models.CharField(max_length=30, null=True)),
                ('cirt', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='ransomware',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rrp.Ransomware'),
        ),
        migrations.AddField(
            model_name='event',
            name='reporters',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='requestUser',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rrp.Users'),
        ),
        migrations.AddField(
            model_name='event',
            name='userAsset',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rrp.Asset'),
        ),
    ]
