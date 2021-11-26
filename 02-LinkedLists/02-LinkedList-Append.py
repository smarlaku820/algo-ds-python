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
    
    def append(self, value):
        """
        append creates a new node, that should be the first step.
        think about all the cases and code it up.
        And since we have created a node, don't forget to increment the length.
        You can return a True, and its completely optional. But if you are 
        calling append methods from other methods, it will be really useful
        to have this method return a bool to tell if its a success or a failure.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.print_ll()