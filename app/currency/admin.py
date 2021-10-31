from django.contrib import admin
from currency.models import Rate
from currency.resources import RateResource

from rangefilter.filters import DateTimeRangeFilter

from import_export.admin import ImportExportModelAdmin



class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        ('created', DateTimeRangeFilter),
    )
    search_fields = (
        'buy',
        'sale',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Rate, RateAdmin)
