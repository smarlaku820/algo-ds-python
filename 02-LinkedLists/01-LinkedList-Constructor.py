class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_ll = LinkedList(4)
my_ll.print_ll()