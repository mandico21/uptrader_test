from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/tags/menu.html')
def draw_menu(menu_name: str) -> dict:
    items = Menu.objects.get(name=menu_name).menu.filter(parent=None)
    return {'items': items}
