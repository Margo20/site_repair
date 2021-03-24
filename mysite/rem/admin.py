from django.contrib import admin
from .models import contactsModel, FooterModel,  DiscountModel, OrderCalculationModel, KapRemModel,  EuroRemModel


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'description', 'published']
    search_fields = ['published']


class FooterAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'published']
    search_fields = ['published']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['phone', 'published']
    search_fields = ['published']


class OrderCalculationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


class KapRemAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


class EuroRemAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'description', 'published']
    search_fields = ['published']


admin.site.register(contactsModel, ContactAdmin)
admin.site.register(FooterModel, FooterAdmin)
admin.site.register(DiscountModel, DiscountAdmin)
admin.site.register(OrderCalculationModel, OrderCalculationAdmin)
admin.site.register(KapRemModel, KapRemAdmin)
admin.site.register(EuroRemModel, EuroRemAdmin)
