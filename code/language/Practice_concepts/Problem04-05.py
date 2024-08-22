"""
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to the
    calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
    can be done on a separate line. After each such input, you should output
    to the Python console what would be displayed on your calculator.
"""

import re
import os

def calculate_interactive():

    view = []
    values= []
    while True:
        input_v = input('>>>')
        view.append(input_v)
        values.append(input_v)
        print(" ".join(view))


        operators = []
        numbers = []
        if input_v == '=':

            for i in values:

                ope = re.findall(r'[+\-/*]',i)
                num = re.findall(r'\d+',i)


                if ope:
                    #se usa extend porque add al final
                    operators.extend(ope)

                if num:
                    numbers.extend(map(int,num))

            result = numbers[0]
            for i in range(len(operators)):
                if operators[i] == '+':
                    result += numbers[i+1]
                elif operators[i] == '-':
                    result -= numbers[i+1]
                elif operators[i] == '*':
                    result *= numbers[i+1]
                elif operators[i] == '/':
                    result /= numbers[i+1]

            print(f"Result: {result}")
            break

calculate_interactive()

