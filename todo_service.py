from list_item import ListItem


class TodoService:

    def __init__(self):
        self.item_root = ListItem('root')
        self.nav_item = self.item_root
        self.item_root.add_child(ListItem('egg'))
        self.item_root.add_child(ListItem('beans'))

    def cd(self, args=''):
        pass

    def add(self, args=''):
        try:
            parts = args.split(' ', maxsplit=1)
            title = parts[1] if len(parts) > 1 else ''
            index = int(parts[0])
            self.nav_item.add_child(ListItem(title), index)
        except ValueError:
            self.nav_item.add_child(ListItem(args))

    def remove(self, args=''):
        try:
            index = int(args)
            self.nav_item.remove_child_by_position(index)
        except ValueError:
            self.nav_item.remove_child_by_title(args)

    def list(self, args=''):
        for index, child in enumerate(self.nav_item.get_children()):
            print(f'{index + 1}. {child.title}')
