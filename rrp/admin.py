from django.contrib import admin
from rrp.models import Users, Event, Ransomware, Asset, RiskLevelAssessment, Information

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'superior', 'cirt', 'reporter')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'requestTime', 'requestUser', 'userAsset', 'ransomware', 'ransomwareName', 'ransomwareType', 'duration', 'riskLevel', 'currentProcess', 'reporter_list')

class AssetAdmin(admin.ModelAdmin):
    list_display = ('assetName', 'assetType', 'dataLevel')

class RansomwareAdmin(admin.ModelAdmin):
    list_display = ('ransomwareName', 'ransomwareType', 'description')

class RiskLevelAssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dataLevel', 'ransomwareType', 'riskLevel')

class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'info')

admin.site.register(Users, UsersAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Ransomware, RansomwareAdmin)
admin.site.register(RiskLevelAssessment, RiskLevelAssessmentAdmin)
admin.site.register(Information, InformationAdmin)
