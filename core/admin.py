from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_phone', 'company', 'project_type', 'delivery_city', 'created_at')
    list_filter = ('project_type', 'budget', 'delivery_city')
    search_fields = ('contact_name', 'contact_phone', 'company', 'delivery_city')
