class ListItem:
    title = ''

    def __init__(self, title):
        self.children = []
        self.title = title

    def add_child(self, child, position=-1):
        for existing_child in self.children:
            if existing_child.title == child.title:
                return
        if position == -1:
            self.children.append(child)
        else:
            self.children.insert(position - 1, child)

    def get_title(self):
        return self.title

    def get_children(self):
        return self.children

    def remove_child_by_title(self, title):
        for child in self.children:
            if child.title == title:
                self.children.remove(child)

    def remove_child_by_position(self, position):
        self.children.remove(position)
