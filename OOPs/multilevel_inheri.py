class A:
    def __init__(self,i=100):
        self.i=i
    def disp(self):
        print("In A")

class B(A):
    def __init__(self,i):
        super().__init__(i)
    def disp(self):
        print("In B")

class C(B):
    def __init__(self,i):
        super().__init__(i)

c=C(50)
print(c.i)
c.disp()

a=A()
print(a.i)

b=B(150)
print(b.i)
    
