import json


import json


class People:

    
    def __init__(self,first_name,last_name,address,phone_number,account_bal=0,account_pin):
       self.first_name = first_name
       self.last_name = last_name
       self.address = address
       self.phone_number = phone_number
       self.account_bal = account_bal
       self.account_pin = account_pin
       
       self.rec_json ={
                'f_name': self.first_name,
                'l_name': self.last_name,
                'adr': self.address,
                'ph_number': self.phone_number,
                'Cash_in_account': self.account_bal,
                'account_pin': self.account_pin
       }

        
    def data_rec_json(self):
        
        with open('record.json','w') as file:
            json.dump(self.rec_json,file,indent=4)

    def update_json(self,info):
        self.info = info
        with open('record.json','r') as file:
            data = json.load(file)
            data.update(self.info)
        
        with open('record.json','w') as file:
            json.dump(data,file,indent=4)

class Employe(People):

    def __init__(self,first_name,last_name,address,phone_number):
        super().__init__(first_name, last_name, address, phone_number)
        pass
    