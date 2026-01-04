from list_item import ListItem


class TodoService:

    def __init__(self):
        self.item_root = ListItem('')
        self.nav_item = self.item_root

    def cd(self, args=''):
        if args == '..':
            if self.nav_item.parent:
                self.nav_item = self.nav_item.parent
        elif args == '/':
            self.nav_item = self.item_root
        else:
            child = next((c for c in self.nav_item.children if c.title == args), None)
            if child:
                self.nav_item = child

    def get_path(self):
        path = []
        path_item = self.nav_item
        while path_item.title:
            path.append(path_item.title)
            path_item = path_item.parent
        path_string = '/'.join(reversed(path))
        return f'{path_string} ' if path_string else ''

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
        for index, child in enumerate(self.nav_item.children, 1):
            print(f'{index}. {child.title}')
