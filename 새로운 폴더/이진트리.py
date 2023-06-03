class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if value < node.value:
            if node.left:
                self._add_node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_node(value, node.right)
            else:
                node.right = Node(value)

    def print_tree(self):
        if not self.root:
            return "Tree is empty"
        else:
            return self._print_tree(self.root)

    def _print_tree(self, node):
        if not node:
            return ''
        else:
            return str(node.value) + ' ' + self._print_tree(node.left) + ' ' + self._print_tree(node.right)
