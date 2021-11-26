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
    
    def pop_first(self):
        """
        pop_first will remove a node from the beginning of the linked list.
        You have to return the node which is popped.
        When we think of use-cases, there are 3 use-cases, that we must handle.
        ie., the linked list is empty
        and when the linked list is not empty and when there is a single node
        in the linked list.
        """
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """
        get will return a node at a particular index.
        think about the value of the index at the very beginning,
        if the index is out of plausible ranges, you must return a None.
        this automatically handles the use-case where the linked list is empty.
        """
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        """
        set will set the value of a particular node at an index.
        you need to handle the value of the index at the very beginning.
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        insert will insert a node at the specified index, first you must create
        a node. 
        We need to think of 3 use-cases, 
        We need to check if the index is valid or not.
        Node will be inserted at the beginning.
        Node will be inserted at the ending.
        Then we will get the position of the node which is 1 down the given index.
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """
        remove will remove a node at the specified index. And you must
        return the node which is removed.
        First handle the index value which is being passed, then if its 
        the removal of the node at the beiginning use pop_first & 
        if it is at the end then use pop.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        Given a linked list reverse it. You need to return the
        self.head pointer to be able to traverse the length of the list.
        if its an empty linked list or there is only one element in the
        list, you return the self.head
        """
        if self.length == 0 or self.length == 1:
            return self.head
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        temp = self.tail
        after = self.tail
        for _ in range(self.length):
            after = after.next
            temp.next = before
            before = temp
            temp = after
        return self.head




my_ll = LinkedList(0)

for i in range(1,10):
    my_ll.append(i)

my_ll.reverse()
my_ll.print_ll()