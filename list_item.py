class ListItem:
    def __init__(self, title):
        self.children = []
        self.title = title
        pass

    def add_child(self, child, position = -1):
        if position == -1:
            self.children.append(child)
        else:
            self.children.insert(position, child)

    def get_title(self):
        return self.title

    def get_children(self):
        return self.children


