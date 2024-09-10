from django import template
from django.urls import resolve
from django.template.context import RequestContext


from menu.models import Menu


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: RequestContext, menu_name: str) -> dict:
    """Заполнение вложенности древовидного меню"""
    path = context['request'].path
    full_path = context['request'].build_absolute_uri()
    current_url_name = resolve(path).url_name
    menu_items = Menu.objects.filter(menu_name=menu_name)
    menu_dict = {}
    
    # присваиваем каждому подпункту статус активности
    for item in menu_items:
        item.is_active = item.get_absolute_url() == full_path or current_url_name == item.named_url
        menu_dict.setdefault(item.parent_id, []).append(item) # {id родителя: [children]}
        
    def build_menu_tree(parent_id: int | None = None) -> list:
        tree = []
        for item in menu_dict.get(parent_id, []):
            children = build_menu_tree(item.id) # рекурсивно заполняем вложенность

            if children and any(child['item'].is_active for child in children):  # Если дочерние элементы активны
                item.is_active = True  # Активировать родителя
                
            tree.append({
                'item': item,
                'children': children
            })
        return tree

    menu_tree = build_menu_tree()
    return {'menu_tree': menu_tree}