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
    
    def pop(self):
        """
        pop removes a node from the linked list, so you better
        don't forget to return the node when you pop a node from the end of the list.
        you need to think about all the edge cases.
        Here we are coding for 3 use cases.
        when there are no nodes, there are more than 2 nodes and a single node.
        start writing code for more than 2 nodes and write an if condition like
        below.
        """
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        """
        prepend will create a new node. this is the first step.
        think about the use-cases, there are 2 use-cases to tackle.
        when there are no nodes in the linked list and when there are
        already some nodes in the linked list.
        Here again, the return value is if you are able to prepend or 
        not, so return a True
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True



my_ll = LinkedList(2)
my_ll.append(3)
my_ll.prepend(1)
my_ll.print_ll()