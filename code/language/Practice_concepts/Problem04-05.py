"""
    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to the
    calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
    can be done on a separate line. After each such input, you should output
    to the Python console what would be displayed on your calculator.
"""
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
            values.remove('=')
            str_values = int(''.join(values))
            print(str_values)
            break

calculate_interactive()




"""
    Write a Python program that simulates a handheld calculator. Your pro-
    gram should process input from the Python console representing buttons
    that are “pushed,” and then output the contents of the screen after each op-
    eration is performed. Minimally, your calculator should be able to process
    the basic arithmetic operations and a reset/clear operation.
"""
