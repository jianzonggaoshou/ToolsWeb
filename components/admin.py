from django.contrib import admin

from .models import Component, Chasis


class ChasisAdmin(admin.ModelAdmin):
    list_display = ['id', 'height', 'wide']


admin.site.register(Chasis, ChasisAdmin)


class ComponentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'submitter']


admin.site.register(Component, ComponentsAdmin)
