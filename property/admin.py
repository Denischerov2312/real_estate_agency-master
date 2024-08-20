from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class Owner_flatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat',]


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number',)
    raw_id_fields = ('liked_by',)
    inlines = [
        Owner_flatsInline,
    ]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'pure_phonenumber')
    inlines = [
        Owner_flatsInline,
    ]
    exclude = ["flats"]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('who_complained',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
