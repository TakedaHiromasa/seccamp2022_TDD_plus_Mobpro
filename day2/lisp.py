# (value, env2) = eval(expr, env)
# env: 処理系の環境（記号表を内部に持つようなデータ構造）
# env2: 更新された環境

class Env:
    def __init__(self) -> None:
        self.funcname
        self.params
        self.body

def eval(expr, env):
    exprsplit = expr.split(' ')
    if exprsplit.pop(0) != '(':
        return None

    if exprsplit.pop(0) == '+':
        sum = 0
        while exprsplit:
            x  = exprsplit.pop(0)
            if x.isdigit():
                sum += int(x)
            elif x == ')':
                break
            else:
                return None
    elif exprsplit.pop(0) == 'defun':
        # ( defun foo ( a ) ( a ) ) ( foo 3 )
        env.funcname = exprsplit.pop(0)
        if exprsplit.pop(0) != '(':
            return None
        while exprsplit:
            x = exprsplit.pop(0)
            if x == ')':
                break
            env.params.append(x)
        if exprsplit.pop(0) != '(':
            return None
        
        while exprsplit:
            x = exprsplit.pop(0)
            if x == ')':
                break
            env.body.append(x)

        if exprsplit.pop(0) != ')':
            return None
        return (None, env)
    else:
        return None
    
    return sum
