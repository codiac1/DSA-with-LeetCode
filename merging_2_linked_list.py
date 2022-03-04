class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, newnode):
        self.__next = newnode


class LinkedList:
    def __init__(self):
        self.__start = None
        self.__tail = None

    def get_start(self):
        return self.__start

    def set_start(self, start):
        self.__start = start

    def get_tail(self):
        return self.__tail

    def set_tail(self, tail):
        self.__tail = tail

    def insertbegin(self, data):
        newnode = Node(data)
        if self.get_start() is None:
            self.__start = self.__tail = newnode
        else:
            self.__tail.set_next(newnode)
            self.set_tail(newnode)

    def delete_begin(self, element):
        if self.get_start().get_data() == element:
            self.set_start(self.get_start().get_next())
        else:
            pass

    def delete_pos(self, data):
        if self.get_start() is None:
            print("empty!")
        else:
            self.temp = self.get_start()
            while (self.temp.get_next().get_data() != data):
                self.temp = self.temp.get_next()
            self.temp.set_next(self.temp.get_next().get_next())

    def display(self):
        if self.get_start() is None:
            print("empty !")
        else:
            self.temp = self.get_start()
            while (self.temp != self.__tail):
                print(self.temp.get_data(), "->", end="  ")
                self.temp = self.temp.get_next()
            print(self.temp.get_data(), "->", end="  ")
            print(None)

    def merge_sorted_list(l1, l2):
        temp = dummy = Node()



L1 = LinkedList()
L1.insertbegin(int(input("enter element :")))
L1.insertbegin(int(input("enter element :")))
L1.insertbegin(int(input("enter element :")))
L1.display()
# L1.delete_pos(int(input("enter element to delete:")))
#L1.delete_begin()
L2 = LinkedList()
L2.insertbegin(int(input("enter element :")))
L2.insertbegin(int(input("enter element :")))
L2.insertbegin(int(input("enter element :")))
L2.display()
L3 = LinkedList()
L3.set_start() merge_sorted_list(L1.get_start(),L2.get_start() )
L3.display()