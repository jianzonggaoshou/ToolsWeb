from django.contrib import admin

from .models import Component


class ComponentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'submitter']


admin.site.register(Component, ComponentsAdmin)