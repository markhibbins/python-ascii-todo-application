from list_item import ListItem


class TodoService:

    def __init__(self):
        self.item_root = ListItem('')
        self.nav_item = self.item_root

    def cd(self, args=''):
        if args == '..' and self.nav_item != self.item_root:
            self.nav_item = self.nav_item.parent
        elif args == '/' and self.nav_item != self.item_root:
            self.nav_item = self.item_root
        else:
            for child in self.nav_item.children:
                if child.title == args:
                    self.nav_item = child

    def get_path(self):
        path=[]
        path_item = self.nav_item
        while path_item.title:
            path.append(path_item.title)
            path_item = path_item.get_parent()
        path_string = '/'.join(reversed(path))
        if path_string: path_string = path_string + ' '
        return path_string

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
