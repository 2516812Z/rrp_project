from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

class Users(models.Model):
    MAX_PASSWORD_LENGTH = 30
    MAX_USERNAME_LENGTH = 30
    MAX_POSITION_LENGTH = 30

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    position = models.CharField(max_length=MAX_POSITION_LENGTH, null=True)
    superior = models.CharField(max_length=MAX_USERNAME_LENGTH, null=True)
    reporter = models.BooleanField(default=False)

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.user.username

class Asset(models.Model):
    MAX_OTHER_LENGTH = 30
    MAX_ANAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 500

    assetName = models.CharField(max_length=MAX_ANAME_LENGTH, primary_key=True)
    assetType = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)
    dataLevel = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.assetName

class Ransomware(models.Model):
    MAX_OTHER_LENGTH = 30
    MAX_RNAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 500

    ransomwareName = models.CharField(max_length=MAX_RNAME_LENGTH, primary_key=True)
    ransomwareType = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH, null=True)

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.ransomwareName

class RiskLevelAssessment(models.Model):
    MAX_OTHER_LENGTH = 30

    id = models.AutoField(primary_key=True)
    dataLevel = models.CharField(max_length=MAX_OTHER_LENGTH)
    ransomwareType = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)
    riskLevel = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.riskLevel


class Event(models.Model):
    MAX_OTHER_LENGTH = 30
    MAX_RNAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 500

    # Event Request
    id = models.AutoField(primary_key=True)
    requestTime = models.DateTimeField(null=True)
    requestUser = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL, default=None)
    userAsset = models.ForeignKey(Asset, null=True, on_delete=models.SET_NULL, default=None)
    ransomware = models.ForeignKey(Ransomware, null=True, on_delete=models.SET_NULL, default=None)
    ransomwareName = models.CharField(max_length=MAX_RNAME_LENGTH, null=True)
    ransomwareType = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)
    ransomAmount = models.IntegerField(null=True)
    duration = models.IntegerField(null=True)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH, null=True)
    evidence = models.ImageField(upload_to='evidence', blank=True)
    # Event Check & Analysis
    riskLevel = models.CharField(max_length=MAX_OTHER_LENGTH, default='L1')
    isKnown = models.BooleanField(default=False)
    recoveryType = models.CharField(max_length=MAX_OTHER_LENGTH, default='Non')
    recoveryTime = models.IntegerField(null=True)
    recoveryInfo = models.CharField(max_length=MAX_DESCRIPTION_LENGTH, null=True)
    handler = models.CharField(max_length=MAX_OTHER_LENGTH, null=True)
    # Event Report
    reporters = models.ManyToManyField(User, blank=True)
    #reporters = models.CharField(max_length=MAX_DESCRIPTION_LENGTH, null=True)
    # Event Recovery
    records = models.CharField(max_length=MAX_DESCRIPTION_LENGTH, null=True)
    # Event AF-Activity
    currentProcess = models.CharField(max_length=MAX_OTHER_LENGTH, default='C&A')

    def reporter_list(self):
        return ','.join([i.username for i in self.reporters.all()])

    class Meta:
        app_label = 'rrp'

    def __str__(self):
        return self.requestUser.user.username





