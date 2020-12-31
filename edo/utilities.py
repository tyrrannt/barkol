
def main_menu_generate(menu_items):
    menu_dict = {}
    result = {}
    for item in menu_items:
        if not item.parent_category:
            menu_dict.update({item.hash_view: list([item.name, item.url_address], )})
        else:
            menu_dict[item.parent_category.hash_view].append([item.name, item.url_address])
    result.update({'nav_menu': menu_items})
    result.update({'nav_hash': menu_dict})
    return result
