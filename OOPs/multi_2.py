class P:
    def disp(self):
        print("In P")

class A:
    def disp(self):
        print("In A")

class B:
    def disp(self):
        print("In B")
        
class C(A,B):
    def disp(self):
        print("In C")

class D(A,B): #to Remove error class D(A,B)
    def disp(self):
        print("In D")

class E(C,D):
    def disp(self):
        print("In E")

r=E()
print(E.__mro__)
   
