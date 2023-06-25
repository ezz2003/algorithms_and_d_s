from BlackRedTree import Tree

if __name__ == '__main__':
    br_tree = Tree()
    br_tree.add_node(23)
    br_tree.add_node(7)
    br_tree.add_node(36)
    br_tree.add_node(34)
    br_tree.add_node(49)

    br_tree.inorder_traversal(br_tree.root)
