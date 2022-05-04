class Computer:
    def writeCode(self,text):
        print("Writes code for ",text)

    def execute(self):
        print("Successfully Executed!!")

class Student:
    def assignment(self,computer,assign): #object of Computer class is paased in Student class
        computer.writeCode(assign) #we're using that object to get the values
        computer.execute()

s1=Student()
c1=Computer()
s1.assignment(c1,"Sorting")
    
        
