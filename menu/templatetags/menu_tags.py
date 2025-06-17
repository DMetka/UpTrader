from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path
    all_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    # Создаем словарь: id -> item
    items_by_id = {item.id: item for item in all_items}
    tree = []

    # Добавляем потомков
    for item in all_items:
        item.children_items = []
        item.is_active = False
        item.is_open = False
        item.is_open_level = False

    for item in all_items:
        if item.parent_id:
            items_by_id[item.parent_id].children_items.append(item)
        else:
            tree.append(item)

    # Отмечаем активный путь
    active_item = None
    for item in all_items:
        if item.get_url() == current_path:
            active_item = item
            break

    def mark_open_path(item):
        item.is_active = True
        while item:
            item.is_open = True
            item = item.parent

    if active_item:
        mark_open_path(active_item)
        for child in active_item.children_items:
            child.is_open = True
            child.is_open_level = True

    return {'menu_tree': tree}