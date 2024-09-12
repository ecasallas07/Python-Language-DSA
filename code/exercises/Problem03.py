"""
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""


def ticktes(diference):

    tickets = [100.000,50.000,20.000,10.000,5.000,2.000,1.000]

    if diference in tickets:
        print(100)
        return diference

    # bill = 0
    result=[]
    co = 0
    print(diference)

    while diference >1.000:
        #tickets
        if co == len(tickets) - 1 :
            co=0


        if tickets[co] <= diference:
            result.append(tickets[co])
            diference -= tickets[co]
            co=0
        else:
            co+=1


    return result



def coins(pay, debt):
    coins = [500, 200, 100, 50]
    difference = pay - debt

    # Convertir la diferencia a centavos
    decimal  = str(difference).split('.')[1]
    coin_pay = int(round(int(decimal) * 100))

    result = []
    for coin in coins:
        while coin_pay >= coin:
            coin_pay -= coin
            result.append(coin)

    print(ticktes(int(difference)))

    return result

print(coins(300.000,20.500))
