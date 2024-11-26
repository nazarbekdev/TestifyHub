from django.contrib import admin
from .models import PartnerRequest, TrialRequest, Subscription, CallCenter


class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'contact_name', 'email', 'phone', 'message', 'created_at')


class TrialRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'created_at')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'plan', 'email', 'phone', 'description', 'created_at')


class CallCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message', 'created_at')


admin.site.register(PartnerRequest, PartnerRequestAdmin)
admin.site.register(TrialRequest, TrialRequestAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(CallCenter, CallCenterAdmin)
