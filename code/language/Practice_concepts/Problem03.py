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


def currency_exchange(pay,debt):
    
    tickets = [100.000,50.000,20.000,10.000,5.000,2.000,1.000]
    coins = [500,200,100,50]

    diference = abs(pay - debt)
    
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
        # coins    
        
        if tickets[co] <= diference:
            result.append(tickets[co])
            diference -= tickets[co]
            co=0
        else:
            co+=1
            
            
    return result
        
print(currency_exchange(300.000,20.500))