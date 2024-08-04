PRICE_COKE = 1100
PRICE_SPRITE = 900
PRICE_VEGEMIL = 1000
PRICE_LETSBE = 800
money = 0

def show_menu():
    menu = ""
    menu+="PRICES "+("="*10)+"\n"
    menu+="1. coke: "+str(PRICE_COKE)+"\n"
    menu+="2. sprite: "+str(PRICE_SPRITE)+"\n"
    menu+="3. vegemil: "+str(PRICE_VEGEMIL)+"\n"
    menu+="4. letsbe: "+str(PRICE_LETSBE)+"\n"
    menu+="5. put in money"+"\n"
    menu+="6. return changes"+"\n"
    menu+="7. display this menu"
    print menu

def select_submit():
    global money
    value = input(str(money)+" won, value(0 to exit): ")

    if value == 1:
        print "1. coke selected"
        if (money >= PRICE_COKE):
            money-=PRICE_COKE
            print "Here's a coke"
        else:
            print "Not enough money"
    elif value == 2:
        print "2. sprite selected"
        if (money >= PRICE_SPRITE):
            money-=PRICE_SPRITE
            print "Here's a sprite"
        else:
            print "Not enough money"
    elif value == 3:
        print "3. vegemil selected"
        if (money >= PRICE_VEGEMIL):
            money-=PRICE_VEGEMIL
            print "Here's a vegemil"
        else:
            print "Not enough money"
    elif value == 4:
        print "4. letsbe selected"
        if (money >= PRICE_LETSBE):
            money-=PRICE_LETSBE
            print "Here's a letsbe"
        else:
            print "Not enough money"
    elif value == 5:
        print "5. money"
        receive_money()
    elif value == 6:
        print "6. returning changes"
        return_changes()
    elif value == 7:
        show_menu()
    elif value == 0:
        return_changes()
        exit(0)
    else:
        print "out of range"

def receive_money():
    global money

    myinput = input("amount: ")
    if (myinput % 50 == 0):
        print myinput, "- OK"
    else:
        print myinput, "- Not OK, in units of 50 won or more"
    money+=myinput

def return_changes():
    global money

    chge_1000s = money / 1000
    money -= 1000 * chge_1000s

    chge_500s = money / 500
    money -= 500 * chge_500s

    chge_100s = money / 100
    money -= 100 * chge_100s

    chge_50s = money / 50
    money -= 50 * chge_50s

    print "1000s:",chge_1000s, "500s:",chge_500s, "100s:",chge_100s, "50s:",chge_50s

# __main__
show_menu()
while True:
    select_submit()
