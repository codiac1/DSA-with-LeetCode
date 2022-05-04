class P:
    def disp(self):
        print("In P")

class A(P):
    def disp(self):
        print("In A")

class B(P):
    def disp(self):
        print("In B")
        
class C(A,B):
    def disp(self):
        print("In C")

class D(C,B):
    def disp(self):
        print("In D")

r=D()
print(D.__mro__)
   
