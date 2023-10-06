from django import template
from menu.models import MenuItem
from django.core.cache import cache 

register = template.Library()

def get_menu(menu_name):
    menu = cache.get(menu_name)
    if menu is None:
        try:
            menu = MenuItem.objects.get(title=menu_name)
            cache.set(menu_name, menu)
        except MenuItem.DoesNotExist:
            menu = None
    return menu


@register.simple_tag
def draw_menu(menu_name, current_path):
    try:
        menu = MenuItem.objects.get(title=menu_name)
        return render_menu(menu, current_path)
    except MenuItem.DoesNotExist:
        return ''

def render_menu(menu, current_path):
    result = '<ul>'
    for item in menu.children.all():
        item_url = item.url or item.named_url
        active_class = 'active' if current_path == item_url else ''
        result += f'<li class="{active_class}"><a href="{item_url}">{item.title}</a>'
        if item.children.exists():
            result += render_menu(item, current_path)
        result += '</li>'
    result += '</ul>'
    return result
