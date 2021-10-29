menu = {"1.Espressso": 35,
                     "2.Cappuccino": 45,
                     "3.Latte": 50,
                     "4.Mocha": 50,
                     "5.Tea": 40,
                     "6.Green Tea(Milk)": 40,
                     "7.Tea(milk)": 40,
                     "8.Lemon tea": 45,
                     "9.Black Tea": 35,
                     "10.Dark Chocolate": 55,
                     "11.Fresh milk": 35,
                     "12.Chocotate": 40}
for i in menu:
    print("{:<20}{:>3}".format(i,menu[i]))