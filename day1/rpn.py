def calc(expr):
    stack = []
    for x in expr.split(" "):
        if x.isdigit():
            stack.append(float(x))
        elif x == '+':
            right = stack.pop()
            left  = stack.pop()
            stack.append(right + left)
        elif x == '-':
            right = stack.pop()
            left  = stack.pop()
            stack.append(left - right)
        elif x == '*':
            right = stack.pop()
            left  = stack.pop()
            stack.append(left * right)
        elif x == '/':
            right = stack.pop()
            left  = stack.pop()
            stack.append(left / right)
        else:
            pass    
    return stack.pop()

def num(expr):
    return False
