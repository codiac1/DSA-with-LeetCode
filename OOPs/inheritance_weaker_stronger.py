class Customer:
    def __init__(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address

    def disp(self):
        print("Name : ", self.name)
        print("Phone : ", self.phone)

        print("Pincode : ",self.address.pin) #Through an Error if Weaker Inheritance(None) is provided

class Address:
    def __init__(self,flat_no,area,pin):
        self.flat_no=flat_no
        self.area=area
        self.pin=pin

a1=Address("102","KV",5018)
'''c1=Customer("Pragya",9450123423,None) ''' #Weaker Inheritance/ Aggregation
c1=Customer("Pragya",9450123423,a1) #Stronger Inheritance/ Composition
c1.disp()
        
