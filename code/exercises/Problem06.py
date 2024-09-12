"""
A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""
import random
def pnishment():
    for i in range(100):
        num = random.randint(1,8)
        options = [3,4,10,15,23,49,34,12]
        if i in options:
            j= ['a',3,'d',10,'c',20,87,'ad','gb']
            print(f" {i} I wi{j[1]} neve{j[num]}r spam my{j[num]} friends agai{j[3]}.")

        print(f" {i} I will never spam my friends again.")

pnishment()
