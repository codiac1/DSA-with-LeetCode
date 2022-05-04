class Student:
    def __init__(self,name):
        self.name=name

    def __eq__(self,name):
        if self.name==name:
            return True
        else:
            return False

def equalchck():
    s1="Hello"
    s2="Hello"
    s3="hello"

    print(s1==s2)
    print(s1==s3)

    st1=Student("Abc")
    st2=Student("Abc")
    print(st1==st2) #2 objects hve different Addresses

equalchck()
    
