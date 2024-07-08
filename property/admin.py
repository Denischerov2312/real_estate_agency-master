from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number',)
    raw_id_fields = ('liked_by',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('who_complained',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
