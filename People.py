import json


class People:

    
    def __init__(self,first_name,last_name,address,phone_number,account_bal=0):
       self.first_name = first_name
       self.last_name = last_name
       self.address = address
       self.phone_number = phone_number
       self.account_bal = account_bal
       
       self.rec_json ={
                'f_name': self.first_name,
                'l_name': self.last_name,
                'adr': self.address,
                'ph_number': self.phone_number,
                'Cash_in_account': self.account_bal
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
        


class Account(People):
  

    def __init__(self,account_bal,checking_acc,saving_rate,fees_on_wid,deposit_amount):
        super().__init__(first_name,last_name,address,phone_number,account_bal)

        self.checking_acc = checking_acc 
        self.savings_rate = saving_rate
        self.fees_on_wid = fees_on_wid
        self.deposit_amount = deposit_amount

    def savings(self):
        pass 

    def deposit(self,deposit_amount):
        
        self.account_bal = self.account_bal + self.deposit_amount


        with open('record.json','r') as file:
            data = json.load(file)
            data['Cash_in_account'] = self.account_bal 
        
        with open('record.json','w') as file:
            json.dump(data,file,indent=4)




        
    #def first_deposit(self,cash_deposit,account_bal):

        #account_bal = account_bal+cash_deposit



if __name__ == '__main__':
    
    print("\n****************WELCOME TO PEOPLE'S BANK***********************\n")
    first_name = input('what is your first name: ')
    last_name =input('what is last name: ')
    address = input('Plsese enter tour address: ')
    phone_number = int(input('Please enter your 10 digit phone number: '))
    bank_obj = People(first_name,last_name,address,phone_number)
    bank_obj.data_rec_json()
    if_emp_or_na = int(input("\nPress 1 if you are employee of People's Bank \n Press 2 if you are Customer: "  ))
    
    if if_emp_or_na == 1:
        print(f"\n++++++++++++++WELCOME TO PEOPLE'S BANK FAMILY {first_name} {last_name}++++++++++++++++++++\n")
        emp = People(first_name,last_name,address,phone_number,account_bal=0)
        sal_empl = { 'Base_salary': 60000 }
        emp.update_json(sal_empl)

    if if_emp_or_na == 2:
        print(f"\n********************Thank You for being a People's Bank Customer {first_name} {last_name}***********************\n")
        Account_type = int(input("\n Press 1 to open Checking Account \n Press 2 to open a Savings  Account:  "))

        if Account_type == 1:
            account = {'Account_type': "Checking Account"}
            bank_obj.update_json(account)
            print(f'\nWould Like to make Deposit {first_name} {last_name} ?\n')
            asking_4_deposit = int(input('Please Enter 1 for "Yes" \n Or 2 for "NO": \n '))

            if asking_4_deposit == 1:
                deposit_amount = int(input('Please Enter the ammount'))
                bank_account = Account(account_bal,checking_acc,saving_rate,fees_on_wid)
                bank_account.deposit(deposit_amount)
               
                





