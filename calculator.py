import re

run = True
previous = 0


def perfom_math():
    global run
    global previous
    equation = input("Enter your equation")
    if(equation == 'quit'):
        print("Byeee")
        run = False
    else:
        answer = eval(equation)
        print(answer)

while run:
    perfom_math()