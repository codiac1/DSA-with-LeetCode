class A:
    def disp(self):
        print("In A")

class B(A):
    def disp(self):
        print("In B")

class C(B):
    def disp(self):
        print("In C")

c=C()
c.disp()

a=A()
a.disp()

b=B()
b.disp()
    
