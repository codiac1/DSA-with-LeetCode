class A(object):
    def disp(self):
        print("In A")

    def __str__(self):  #Overriding and Polymorphism Concept
        return "Object of Class A"

class B(A):
    def disp(self):
        print("In B")

    def __repr__(self):  #Overriding and Polymorphism Concept
        return "Object of Class B"

    
a=A()
a.disp()

b=B()
b.disp()

print(b.__str__())
print(b)
print(b.__repr__())

print(dir(object))
