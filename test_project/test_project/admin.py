from django.contrib import admin
from .models import *


class OrderInline(admin.TabularInline):
    model = Order


class UserAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


admin.site.register(Users, UserAdmin)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Subcategories)
admin.site.register(Question)
admin.site.register(Order)