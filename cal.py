def fun(x,y,op):
  if op == '+':
    return x + y
  elif op == '-':
    return x - y
  elif op == '*':
    return x * y
  elif op == '/':
    if y != 0:
      return x / y
    else:
      return "Error: Division by zero"
  else:
    return "Error: Invalid operator"
 
def mul(a,b):
    return a*b
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
def floor_div(a, b):
    a//b
def power(a, b):
  return a ** b
def mod(a, b):
  if b != 0:
    return a % b
  else:
    return "Error: Division by zero"