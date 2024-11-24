from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

@hooks.register('register_admin_menu_item')
def register_hello_world_menu_item():
    return MenuItem('Hello World', '/admin/hello_world/', classnames='icon icon-folder-open-inverse')
