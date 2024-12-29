from django.contrib import admin
from .models import GBVCenter, Message, IncidentReport

class GBVCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_info')
    search_fields = ('name', 'address', 'contact_info')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'anonymous', 'content', 'timestamp')
    list_filter = ('anonymous', 'timestamp')
    search_fields = ('content',)

class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'timestamp', 'status', 'recommendation')
    list_filter = ('status', 'timestamp')
    search_fields = ('description',)
    actions = ['mark_as_reviewed']

    def mark_as_reviewed(self, request, queryset):
        queryset.update(status='Reviewed')
    mark_as_reviewed.short_description = "Mark selected incidents as reviewed"

admin.site.register(GBVCenter, GBVCenterAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(IncidentReport, IncidentReportAdmin)


