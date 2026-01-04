class ListItem:

    def __init__(self, title, parent=None):
        self.children = []
        self.title = title
        self.parent = parent

    def add_child(self, child, position=-1):
        if any(c.title == child.title for c in self.children):
            return
        child.parent = self
        if position == -1:
            self.children.append(child)
        else:
            self.children.insert(position - 1, child)

    def remove_child_by_title(self, title):
        self.children = [c for c in self.children if c.title != title]

    def remove_child_by_position(self, position):
        if 0 <= position - 1 < len(self.children):
            del self.children[position - 1]
