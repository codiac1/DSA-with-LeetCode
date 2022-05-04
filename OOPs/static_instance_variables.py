class Abc:
    counter=0 #static variable or class variable
    def __init__(self,a=10,b=20):
        self.a=a  #Instance variable
        self.b=b  #Instance variable
        #self.counter = self.a+self.b
    def disp(self):
        print("a : ",self.a)
        print("b : ",self.b)
        print("With creating object, value of Counter : ",self.counter)
        print("Without creating object, value of Counter : ",Abc.counter)

obj1=Abc()
obj2=Abc(1,2)
obj1.disp()
obj2.disp()
obj1.counter = 6
obj2.disp()
