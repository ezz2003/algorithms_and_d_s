class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = 'Red'


def rotate_left(node):
    right_node = node.right
    node.right = right_node.left
    right_node.left = node
    right_node.color = node.color
    node.color = 'Red'
    return right_node


def flip_colors(node):
    node.color = 'Red'
    node.left.color = 'Black'
    node.right.color = 'Black'


def rotate_right(node):
    left_node = node.left
    node.left = left_node.right
    left_node.right = node
    left_node.color = node.color
    node.color = 'Red'
    return left_node


class Tree:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if not node:
            return False
        return node.color == 'Red'

    def add_node(self, key, value=None):
        self.root = self._add_node(self.root, key, value)
        self.root.color = '~Black'

    def _add_node(self, node, key, value):
        if not node:
            return Node(key, value)
        if key < node.key:
            node.left = self._add_node(node.left, key, value)
        elif key > node.key:
            node.right = self._add_node(node.right, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            flip_colors(node)

        return node

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, node.color)
            self.inorder_traversal(node.right)