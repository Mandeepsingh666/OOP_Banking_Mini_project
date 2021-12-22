# Springboard Data Engineering Banking System Mini-Project
## Motivation
### In this project I tried to demonstrate my understanding of Object Oriented Programming and Inheritance.
#### Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.
#### Inheritance is a mechanism in which one class acquires the property of another class. For example, a child inherits the traits of his/her parents. With inheritance, we can reuse the fields and methods of the existing class.



## IN this Project i wrote 3 Classes. 
- People (Parent Class,)  
- Account(Child Class) 
- Services(Child Class)


## Command Line Interface User Interaction (requires Python Version 3)

```bash
python3 People.py
```

## Package needed.
```python
pip install json 
```

## Demo Number 1. 
- here i opened a checking account.
- deposited $1000 and then withdraw $999.
- Also got aproved a line of credit bassed on my Credit score @ very low interest rate Because of excelent credit score.


```bash
****************WELCOME TO PEOPLE'S BANK***********************

what is your first name: Mandeep  
what is last name: Singh
Plsese enter your address: 101-ave
Please enter your 10 digit phone number: 9177174941

Press 1 if you are employee of People's Bank 
Press 2 if you are Customer: 2

********************Thank You for being a People's Bank Customer Mandeep Singh***********************


Press 1 to open Checking Account 
Press 2 to open a Savings  Account:  1

Would Like to make Deposit Mandeep Singh ?


Please Enter 1 for "Yes" 
Or 2 for "NO": 1
Please Enter the ammount: 1000
Your Account Balance is :$1000

Do you need a line of credit Mandeep Singh ?

Please Enter 1 for "Yes" or Enter 2 For "NO" :1
What is your Credit Score Mandeep Singh ?550

You are aproved for line of credit :15000 
Interest rate: 0.04
Number of Months :60
monthly payments :
276.25

Would You like withdraw some money Mandeep Singh?

Press 1 For "Yess" or 
Press 2 for "NO" :1
Plase enter a amount that you would like to withdraw: 999
Your Account Balance is :$1
++++++++++++++++++Account Summry++++++++++++++++++++++++
{
    "first_name": "Mandeep",
    "l_name": "Singh",
    "adr": "101-ave",
    "ph_number": 9177174941,
    "Cash_in_account": 1,
    "Account_type": "Checking Account",
    "Principal": 15000,
    "rate": "4%",
    "Months": 60
}
```
## Demo number 2. 
- here I am employee of the Bank.
- my salary has been displayed in output.
- also got aproved for line of credit for high interest rate because of bad credit score. 

```bash 
****************WELCOME TO PEOPLE'S BANK***********************

what is your first name: Madeep singh
what is last name: multani
Plsese enter your address: 101-ave
Please enter your 10 digit phone number: 9177174941

Press 1 if you are employee of People's Bank 
Press 2 if you are Customer: 1

++++++++++++++WELCOME TO PEOPLE'S BANK FAMILY Madeep singh multani++++++++++++++++++++

your base salary is $60000

Would Like to make Deposit Madeep singh multani ?


Please Enter 1 for "Yes" 
Or 2 for "NO": 1
Please Enter the ammount: $1000
Your Account Balance is :$1000

Do you need a line of credit Madeep singh multani ?

Please Enter 1 for "Yes" or Enter 2 For "NO" :1 
What is your Credit Score Madeep singh multani ?550

You are aproved for line of credit :15000 
Interest rate: 0.04
Number of Months :60
monthly payments :
276.25

Would You like withdraw some money Madeep singh multani?

Press 1 For "Yess" or 
Press 2 for "NO" :1
Plase enter a amount that you would like to withdraw: 999
Your Account Balance is :$1
++++++++++++++++++Account Summry++++++++++++++++++++++++
{
    "first_name": "Madeep singh",
    "l_name": "multani",
    "adr": "101-ave",
    "ph_number": 9177174941,
    "Cash_in_account": 1,
    "Base_salary": 60000,
    "Principal": 15000,
    "rate": "4%",
    "Months": 60
}
```
### Demo Number 3.
- Here i Opended a Savings account @  0.03% saving account intrest rate.
- also got aproved for credit line @ medium interest rate because of good credit score.
```bash
****************WELCOME TO PEOPLE'S BANK***********************

what is your first name: Mandeep 
what is last name: singh
Plsese enter your address: 101-ave
Please enter your 10 digit phone number: 9177174491

Press 1 if you are employee of People's Bank 
Press 2 if you are Customer: 2

********************Thank You for being a People's Bank Customer Mandeep singh***********************


Press 1 to open Checking Account 
Press 2 to open a Savings  Account:  2

Our Bank Provide Very Compatative rate of:0.03%


Would Like to make Deposit Mandeep singh ?


Please Enter 1 for "Yes" 
Or 2 for "NO": 1
Please Enter the ammount: 1000
Your Account Balance is :$1000

Do you need a line of credit Mandeep singh ?

Please Enter 1 for "Yes" or Enter 2 For "NO" :1
What is your Credit Score Mandeep singh ?650

You are aproved for line of credit :15000 
Interest rate: 0.04
Number of Months :60
monthly payments :
276.25

Would You like withdraw some money Mandeep singh?

Press 1 For "Yess" or 
Press 2 for "NO" :1
Plase enter a amount that you would like to withdraw: 999
Your Account Balance is :$1
++++++++++++++++++Account Summry++++++++++++++++++++++++
{
    "first_name": "Mandeep",
    "l_name": "singh",
    "adr": "101-ave",
    "ph_number": 9177174491,
    "Cash_in_account": 1,
    "Account_type": "Saveings Account",
    "savings_intrest_rate": 0.03,
    "Principal": 15000,
    "rate": "4%",
    
```





