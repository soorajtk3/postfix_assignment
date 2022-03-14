import re


def postfix(value):
    stack = []
    operator = []
    charlist = []
    for i in value:
        if i == '+' or i == '*' or i == '/' or i == '-':
            operator.append(i)
        if i.isdigit():
            charlist.append(i)
        if(len(charlist) < len(operator)):
            return "error"
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
