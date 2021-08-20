Name = input('Type name and last name : ')
Old = int(input('type your old : '))
income= int(input('type your incomde : '))
tax= None
if income>=70000:
    tax = income * .28
elif 50000 <= income:
    tax = income * .16
elif 20000 <= income:
    tax = income * .12
else:
    tax = income * .07
if Old<21 or Old>60:
    tax = tax * .6
print('Username : {}\nAge : {}\nIncome : {} Bath\nHave to pay tax : {} Bath'.format(Name,Old,income,tax))