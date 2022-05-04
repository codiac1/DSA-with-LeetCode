from abc import *

class A(ABC):
    def __init__(self):
        self.i=5
    @abstractmethod
    def disp(self): #coz of abstract method,we can't create its object
        pass
    def show(self): #concrete method or normal method
        print("Abstract class A")

class B(A):
    def disp(self): #compulsion to child class to override the abstract method here
        print("Abstract class B")
        print(self.i)

b=B()
b.show()
b.disp()

