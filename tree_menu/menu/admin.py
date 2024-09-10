from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'named_url', 'parent', 'menu_name']
    list_display_links = ['id', 'title']
    prepopulated_fields = {'url': ('title',)}
