class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None

    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=None
        else:
            self.new_node=Node(data)
            self.temp=self.head
            while(self.temp.next != None):
                self.temp=self.temp.next
            self.temp.next=self.new_node
            self.new_node=None
            
    def mid_element(self):
        self.slow=self.head
        self.fast=self.head
        print(self.head)
        print(self.fast.data)
        print(self.fast.next)
        while(self.fast != None):
            self.fast=self.fast.next
            self.fast = self.fast.next
            if(self.fast == None):
                break
            else:
                self.slow=self.slow.next
        print("Mid Element is -> ",self.slow.data)

l1=LinkedList()
print("\nFor Insertion at End ")
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.mid_element()
