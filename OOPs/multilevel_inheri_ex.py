class A:
    def disp(self):
        print("In A")

class B(A):
    pass
    #def disp(self):
        #print("In B")
        
class C(A):
    pass
    #def disp(self):
        #print("In C")

class D(B,C):
    pass

r=D()
r.disp()
   
