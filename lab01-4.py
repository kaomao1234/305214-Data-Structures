with open('fruit.txt',mode='r') as f: 
    fruit_value = {i.split(' ')[0]:int(i.split(' ')[1]) for i in f.read().splitlines()} 
    customer_buy = {}
    for i in fruit_value:
        customer_buy.update({i:int(input('How many kilograms of {} do you want to buy?\n'.format(i)))*fruit_value[i]}) 
    customer_buy_lst = sorted(list(customer_buy.values()))
    for i in customer_buy:
        if customer_buy[i]== customer_buy_lst[len(customer_buy_lst)-1]: 
            print('{} is the most expensive !'.format(i))
    print('Customer has to pay {} Bath.'.format(sum(customer_buy_lst)))