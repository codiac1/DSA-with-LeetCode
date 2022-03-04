class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def insert_begin(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            self.new_node = Node(data)
            self.new_node.next = self.head
            self.head = self.new_node

    def display(self):
        if self.head is None:
            print("Underflow!!")
        else:
            self.temp = self.head
            while (self.temp != None):
                print(str(self.temp.data) + " -> ", end=" ")
                self.temp = self.temp.next
            print("None")

def merge(l1, l2):
    temp = head_ptr = Node()
    while l1 and l2:
        if l1.data <= l2.data:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if (l1):
        temp.next = l1
    if (l2):
        temp.next = l2
    return head_ptr.next


l1 = LinkedList()
print("\nFirst Sorted Linked List : ")
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.display()

l2 = LinkedList()
print("\nSecond Sorted Linked List : ")
l2.insert_begin(int(input("enter element : ")))
l2.insert_begin(int(input("enter element : ")))
l2.insert_begin(int(input("enter element : ")))
l2.display()

l3 = LinkedList()
print("\nMerging First and Second Linked List : ")
l3.head = merge(l1.head, l2.head)
l3.display()