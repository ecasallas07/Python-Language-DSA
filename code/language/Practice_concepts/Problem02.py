
"""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""


def validate(num):
    if num < 2:
        return "Invalid input. Please enter a positive integer greater than 2."
    else:
        counter = 0
        while True:
            num = num /2
            counter+=1
            if num < 2:
                return counter
                
                

print(validate(10))            
