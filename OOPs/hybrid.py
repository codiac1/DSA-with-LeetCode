#Hybrid Inheritence and Method Resolution Order
class A():
    def m(self):
        print("method m of A called")

class B():
    def m(self): # if we do pass here then method m of C is called not A
        print("method m of B called")

class C(A):
    def m(self):
        print("method m of C called")

class D(B,C):
    pass

d=D()
d.m()
