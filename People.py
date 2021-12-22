import json
from json.decoder import JSONDecodeError


class People:

    
    def __init__(self,first_name,last_name,address,phone_number,account_bal=0,):
       self.first_name = first_name
       self.last_name = last_name
       self.address = address
       self.phone_number = phone_number
       self.account_bal = account_bal
       
       
       self.rec_json ={
                'first_name': self.first_name,
                'l_name': self.last_name,
                'adr': self.address,
                'ph_number': self.phone_number,
                'Cash_in_account': self.account_bal,
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

    def append_json(self,new_data):

        with open("record.json", "r+") as file:
            data = json.load(file)
            data.update(new_data)
            file.seek(0)
            json.dump(data, file,indent=4)

    

class Account(People):
  

    def __init__(self,account_bal,deposit_amount):
        super().append_json
        super().update_json
        self.deposit_amount = deposit_amount
        self.account_bal =account_bal


    def show_balance(self):
        data  = open('record.json')
        bio_data= json.load(data)
        data.close()
        balance = bio_data['Cash_in_account']

        print(f'Your Account Balance is :${balance}')

        


    def deposit(self,deposit_amount):
     
        self.account_bal = self.account_bal + self.deposit_amount
        balance  = {'Cash_in_account': self.account_bal}

        Account.append_json(self,balance)
        Account.show_balance(self)
        

    def withdraw(self,amount):
        self.amount = amount
        json_file = open("record.json")
        variables = json.load(json_file)
        json_file.close()
        variables['Cash_in_account']= variables['Cash_in_account'] - self.amount

        
        Account.update_json(self,variables)
        Account.show_balance(self)


    def account_summry(self):
        summry = open('record.json')
        data = json.load(summry)
        summry.close()
        print('++++++++++++++++++Account Summry++++++++++++++++++++++++')
        print(json.dumps(data, sort_keys=False, indent=4))

class Services(People):
    
    def __init__(self,credit_score):
        super().append_json
        self.credit_score = credit_score

    def monthly_payment(self,credit_score):
        
        def monthly_instalments(P,rate,months):
            payment = (rate/12) * (1/(1-(1+rate/12)**(-months)))*P
            return round(payment,2)



        if credit_score in  range(0,550):
            P = 5000
            rate = 0.12
            months = 60
            info = {"P":5000,
            'rate':'12%',
            'Months':60}
            
            Services.append_json(self,info)

            print(f"\nYou are aproved for line of credit :{P} \nInterest rate: {rate}\nNumber of Months :{months}\nmonthly payments :")
            print(monthly_instalments(P,rate,months))


        elif credit_score in range(551,650):
            P = 10000
            rate = 0.08
            months = 60
            info = {"P":1000,
            'rate':'8%',
            'Months':60}
            Services.append_json(self,info)

            print(f"\nYou are aproved for line of credit :{P} \nInterest rate: {rate}\nNumber of Months :{months}\nmonthly payments :")
            print(monthly_instalments(P,rate,months))

        else :
            P = 15000
            rate = 0.04
            months = 60
            info = {"P":15000,
            'rate':"4%",
            'Months':60}
            Services.append_json(self,info)

            print(f"\nYou are aproved for line of credit :{P} \nInterest rate: {rate}\nNumber of Months :{months}\nmonthly payments :")
            print(monthly_instalments(P,rate,months))





if __name__ == '__main__':
    
    print("\n****************WELCOME TO PEOPLE'S BANK***********************\n")
    first_name = input('what is your first name: ')
    last_name =input('what is last name: ')
    address = input('Plsese enter your address: ')
    phone_number = int(input('Please enter your 10 digit phone number: '))
    bank_obj = People(first_name,last_name,address,phone_number)
    bank_obj.data_rec_json()
    if_emp_or_na = int(input("\nPress 1 if you are employee of People's Bank \nPress 2 if you are Customer: "  ))
    
    if if_emp_or_na == 1:
        print(f"\n++++++++++++++WELCOME TO PEOPLE'S BANK FAMILY {first_name} {last_name}++++++++++++++++++++\n")
        emp = People(first_name,last_name,address,phone_number,account_bal=0)
        sal_empl = { 'Base_salary': 60000 }
        emp.update_json(sal_empl)
        print('your base salary is ${Base_salary}'.format(**sal_empl))
        print(f'\nWould Like to make Deposit {first_name} {last_name} ?\n')
        asking_4_deposit = int(input('\nPlease Enter 1 for "Yes" \nOr 2 for "NO": '))


        if asking_4_deposit == 1:
            account_bal = 0
            deposit_amount = int(input('Please Enter the ammount: '))
            bank_account = Account(account_bal,deposit_amount)
            bank_account.deposit(deposit_amount)

        if asking_4_deposit == 2:
            summry = Account(account_bal,deposit_amount)
            summry.account_summry()
           


    if if_emp_or_na == 2:
        print(f"\n********************Thank You for being a People's Bank Customer {first_name} {last_name}***********************\n")
        Account_type = int(input("\nPress 1 to open Checking Account \nPress 2 to open a Savings  Account:  "))

        if Account_type == 1:
            account = {'Account_type': "Checking Account"}
            bank_obj.update_json(account)
            print(f'\nWould Like to make Deposit {first_name} {last_name} ?\n')
            asking_4_deposit = int(input('\nPlease Enter 1 for "Yes" \nOr 2 for "NO": '))


            if asking_4_deposit == 1:
                account_bal = 0
                deposit_amount = int(input('Please Enter the ammount: '))
                bank_account = Account(account_bal,deposit_amount)
                bank_account.deposit(deposit_amount)
                
            if asking_4_deposit ==2:
               
                summry = Account(account_bal,deposit_amount)
                summry.account_summry()

        if Account_type == 2:
            account = {'Account_type': "Saveings Account"}
            rate = {'savings_intrest_rate':0.03}
            bank_obj.update_json(account)
            bank_obj.update_json(rate)
            print('\nOur Bank Provide Very Compatative rate of:{savings_intrest_rate}%\n'.format(**rate))
            print(f'\nWould Like to make Deposit {first_name} {last_name} ?\n')
            asking_4_deposit = int(input('\nPlease Enter 1 for "Yes" \nOr 2 for "NO": '))

            if asking_4_deposit == 1:
                account_bal = 0
                deposit_amount = int(input('Please Enter the ammount: '))
                bank_account = Account(account_bal,deposit_amount)
                bank_account.deposit(deposit_amount)

            if asking_4_deposit == 2:
                summry = Account(account_bal,deposit_amount)
                summry.account_summry()

    print(f'\nDo you need a line of credit {first_name} {last_name} ?\n')
    l_credit = int(input('Please Enter 1 for "Yes" or Enter 2 For "NO" :'))

    if l_credit == 1:
        credit_score = int(input(f'What is your Credit Score {first_name} {last_name} ?'))
        credit_line = Services(credit_score)
        credit_line.monthly_payment(credit_score)

    if l_credit ==2:
        
        summry = Account(account_bal,deposit_amount)
        summry.account_summry()


    print(f'\nWould You like withdraw some money {first_name} {last_name}?')
    withdraw_amt = (int(input('\nPress 1 For "Yess" or \nPress 2 for "NO" :')))

    if withdraw_amt == 1:
        amount = int(input('Plase enter a amount that you would like to withdraw: '))
        withdraw = Account(account_bal,deposit_amount)
        withdraw.withdraw(amount)
    
    if withdraw_amt ==2:
        
        summry = Account(account_bal,deposit_amount)
        summry.account_summry()

    summry = Account(account_bal,deposit_amount)
    summry.account_summry()


  