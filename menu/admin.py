from django.contrib import admin

from menu.models import Menu, SubMenu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', ]
    list_editable = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'menu', 'parent', ]
    list_editable = ['name', 'slug', 'menu', 'parent', ]
    prepopulated_fields = {'slug': ('name',)}
