class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create a node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert(self, index, value):
        # create a node at the required position
        req_node = Node(value)
        temp = self.head
        for i in range(index-2):
            self.head = self.head.next
        req_node.next = self.head.next
        self.head.next = req_node
        self.head = temp
        self.length+=1

    def pop(self):
        temp = self.head
        for i in range(self.length-2):
            self.head = self.head.next
        self.head.next = None
        self.head = temp
        self.length-=1
        
    def prepend(self, value):
        # create a node at the beginning
        start_node = Node(value)
        temp = self.head
        self.head = start_node
        self.head.next = temp
        self.length+=1


    def append(self, value):
        # create a node at the ending
        end_node = Node(value)
        self.tail = end_node
        temp = self.head
        for i in range(self.length-1):
            self.head = self.head.next
        self.head.next = end_node
        self.head = temp
        self.length+=1


    def remove(self, index):
        temp = self.head
        for i in range(index-2):
            self.head = self.head.next
        self.head.next = self.head.next.next






def print_ll(linked_list):
    temp = linked_list.head
    for i in range(linked_list.length):
        print(linked_list.head.value)
        linked_list.head=linked_list.head.next
    linked_list.head = temp

my_linkedlist = LinkedList(4)
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)
for i in range(90,93):
    my_linkedlist.append(i)
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)
my_linkedlist.prepend(1)
my_linkedlist.prepend(2)
my_linkedlist.prepend(3)
my_linkedlist.insert(5,5)
my_linkedlist.insert(6,6)
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)
print("About to Pop!!")
my_linkedlist.pop()
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)
print("About to Pop!!")
my_linkedlist.pop()
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)
print("About to Pop!!")
my_linkedlist.pop()
print("There are {} items in the linked list".format(my_linkedlist.length))
# print("Head is at {}".my_linkedlist.head.value)
# print("Tail is at {}".my_linkedlist.tail.value)
print_ll(my_linkedlist)