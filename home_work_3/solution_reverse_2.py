class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node


def console_out(head):
    it = head
    if not it:
        print("list is empty")
    while it:
        print(it.data, end="  " if it.next else '\n')
        it = it.next


def my_reverse(head):
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node, curr_node = curr_node, next_node
    return prev_node


my_list = LinkedList()
for i in range(1, 56):
    my_list.append(i)

console_out(my_list.head)
console_out(my_reverse(my_list.head))
