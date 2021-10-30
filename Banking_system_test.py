

if __name__ == '__main__':
    bannk_obj = Account()
    print("\n****************WELCOME TO PEOPLE'S BANK***********************\n")
    first_name = input('what is your first name: ')
    last_name =input('what is last name: ')
    address = input('Plsese enter tour address: ')
    phone_number = int(input('Please enter your 10 digit phone number: '))
    bannk_obj.data_rec_json(first_name,last_name,address,phone_number,account_bal=0)
    depo_or_wid = int(input('Press 1 for deposit \n Press 2 for withdrawal :'))
    
    if depo_or_wid == 1:
        cash_deposit = int(input('Please enter the amount you want to deposit'))
        bannk_obj.first_deposit(cash_deposit,account_bal=0)