def InvalidCard as e:
    return "Invalid Card No"

def LowBalance as e:
    return "Invalid Card No"
    

class Customer:
    def __init__(self,card_id,cname,balance):
        self.card_id=card_id
        self.cname=cname
        self.balance=balance

c1=Customer(101,"Abc1",10000)
c2=Customer(102,"Abc2",5000)

cust_dict={c1.card_id:c1, c2.card_id:c2}

def check_balance(card_id,cost):
    if cust_dict[card_id].balance>=cost:
        return True
    else:
        raise Exception("Insufficient Balanace!!") #return False

def check_cards(card_id):
    if card_id in cust_dict.keys():
        return True
    else:
        raise Exception("Card Number Mismatch!!") #return False

while(True):
    card_id=int(input("Enter Card Number : "))
    cost=int(input("Enter Cost : "))
    try:
        if check_cards(card_id):
            if check_balance(card_id,cost):
                print("Possible !!")
                break
            else:
                print("Not Possible !!")
    except Exception as e:
        print(e)
        
    
    



    
            


