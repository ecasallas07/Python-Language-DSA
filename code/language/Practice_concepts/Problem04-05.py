"""
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to the
    calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
    can be done on a separate line. After each such input, you should output
    to the Python console what would be displayed on your calculator.
"""

import re
def calculate_interactive():

    view = []
    values= []
    while True:
        input_v = input('>>>')
        view.append(input_v)
        values.append(input_v)
        print(" ".join(view))

        if input_v == '=':

            # TODO: solution operation numbers and operators
            operators = []
            rr_op =[]
            ar_num = []
            for i in values:
                op = re.findall(r'[+\-/*]',i)
                num = re.findall(r'\d+',i)
                if op:
                    rr_op.append(op)
                if num:
                    ar_num.append(num)

            for i in range(len(rr_op)):
                count = 0
                match rr_op[i]:
                    case '+':
                        if i == 0:
                            count = ar_num.pop(i) + ar_num.pop(i+1)
                        else:
                            count += ar_num[]

            break

calculate_interactive()




"""
    Write a Python program that simulates a handheld calculator. Your pro-
    gram should process input from the Python console representing buttons
    that are “pushed,” and then output the contents of the screen after each op-
    eration is performed. Minimally, your calculator should be able to process
    the basic arithmetic operations and a reset/clear operation.
"""
