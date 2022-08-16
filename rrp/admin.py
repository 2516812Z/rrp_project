from django.contrib import admin
from rrp.models import Users, Event, Ransomware, Asset

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'superior')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'requestTime', 'requestUser', 'assetType', 'ransomwareName', 'ransomwareType', 'riskLevel', 'currentProcess')

class AssetAdmin(admin.ModelAdmin):
    list_display = ('assetName', 'assetType', 'dataLevel')

class RansomwareAdmin(admin.ModelAdmin):
    list_display = ('ransomwareName', 'ransomwareType', 'description')

admin.site.register(Users, UsersAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Ransomware, RansomwareAdmin)
