from django.contrib import admin
from rrp.models import Users, Event

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'superior')

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'requestTime', 'requestUser', 'assetType', 'ransomwareName', 'ransomwareType', 'riskLevel', 'currentProcess')

admin.site.register(Users, UsersAdmin)
admin.site.register(Event, EventAdmin)