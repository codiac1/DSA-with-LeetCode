class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        if(len(self.__customer_id)==6) and (self.__customer_id.startswith('1') ):
            return True
        else:
            return False
        

class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__freight_id=0
        self.__freight_charge=0
        
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_weight(self):
        return self.__weight

    def get_distance(self):
        return self.__distance

    def get_freight_id(self):
        return self.__freight_id

    def get_freight_charge(self):
        return self.__freight_charge

    

    def validate_weight(self):
        if(self.__weight % 5==0):
            return True
        else:
            return False

    def validate_distance(self):
        if(self.__distance in range(500,5001)):
            return True
        else:
            return False
        

    def forward_cargo(self):
        if self.get_from_customer().validate_customer_id() and self.get_recipient_customer().validate_customer_id() and self.validate_weight() and self.validate_distance():
            Freight.counter = Freight.counter+2
            self.__freight_id = Freight.counter
            self.__freight_charge = (self.get_weight()*150) + (self.get_distance()*60)
        else:
            self.__freight_charge = 0
        return self.__freight_charge
            

c1=Customer('123456','Pragya','Abc')
c2=Customer('122226','Pranav','pqr')

f1=Freight(c1,c2,75,1200)
print(f1.forward_cargo())
        
        
