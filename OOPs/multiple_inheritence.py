class A:
    def __init__(self):
        self.i=5
    def disp(self):
        print("In A")

class B:
    def __init__(self):
        self.j=7
    def disp(self):
        print("In B")
        
class C(A,B):
    def __init__(self):
        super().__init__()
        #B.__init__()

c=C()
print(c.i)
#print(c.j)
c.disp()
print(C.__mro__) #Method Resolution Order , the order in which C class inherits
                 #(First A then B)
    
    
