import re


def postfix(value):
    stack = []
    for i in value:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            number1 = stack.pop()
            number2 = stack.pop()
            stack.append(number1+number2)
        elif i == '-':
            number1 = stack.pop()
            number2 = stack.pop()
            stack.append(number1-number2)
        elif i == '/':
            number1 = stack.pop()
            number2 = stack.pop()
            stack.append(number1/number2)
        elif i == '*':
            number1 = stack.pop()
            number2 = stack.pop()
            stack.append(number1*number2)
        else:
            return False
    return stack.pop()
