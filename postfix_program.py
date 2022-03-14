def postfix(value):
    stack = []
    numbers = "0123456789"
    for i in value:
        if i in numbers:
            stack.append(int(i))
        elif i == '+':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.append(int(digit1)+int(digit2))
        elif i == '-':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.append(int(digit1)-int(digit2))
        elif i == '/':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.append(int(digit1)/int(digit2))
        elif i == '*':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.append(int(digit1)*int(digit2))
    return stack.pop()


(postfix("452*+"))
