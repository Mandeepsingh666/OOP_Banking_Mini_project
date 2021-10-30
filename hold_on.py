import json


class People:

    
    def __init__(self,first_name,last_name,address,phone_number):
       self.firstname = first_name
       self.last_name = last_name
       self.address = address
       self.phone_number = phone_number
       
    def data_rec_json(self):
        
        rec_json = {
                'f_name': self.first_name,
                'l_name': self.last_name,
                'adr': self.address,
                'ph_number': self.phone_number,
                'Cash_in_account': self.account_bal
                }
        

        with open('record.json','w') as info:
            json.dump(rec_json,info,indent=4)
            
class Acount(People):

    def __init__(self, first_name, last_name, address, phone_number,checking_account,savings_account):
        super().__init__(first_name, last_name, address, phone_number)
        self.checking_account = checking_account
        self.savings_account = savings_account
        



        
        
    #def first_deposit(self,cash_deposit,account_bal):

        #account_bal = account_bal+cash_deposit
            
        

        


            










if __name__ == '__main__':
    
    print("\n****************WELCOME TO PEOPLE'S BANK***********************\n")
    first_name = input('what is your first name: ')
    last_name =input('what is last name: ')
    address = input('Plsese enter tour address: ')
    phone_number = int(input('Please enter your 10 digit phone number: '))
    bank_obj = People(first_name,last_name,address,phone_number)
    bank_obj.data_rec_json(first_name,last_name,address,phone_number)
    depo_or_wid = int(input('Press 1 for deposit \n Press 2 for withdrawal :'))
    
    if depo_or_wid == 1:
        cash_deposit = int(input('Please enter the amount you want to deposit'))
        bank_obj.first_deposit(cash_deposit,account_bal=0)