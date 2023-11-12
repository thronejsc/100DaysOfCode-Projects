# Calculator App (Simple)
from art import logo

# Add
def add(a,b):
  """Take the two numbers and return the sum"""
  return a + b
# Subtract
def subtract(a,b):
  """Take the two numbers and return the difference"""
  return a - b
# Multiply
def multiply(a, b):
  """Take the two numbers and return the product"""
  return a * b
# Divide
def divide(a, b):
  """Take the two numbers and return the quotient"""
  return a * b

# Operators
operators = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  print(logo)
  finished = False
  a = float(input("Whats is the first number? "))
  for i in operators:
    print(f"\n{i}")
    
  while finished != True:
    operation = input("Pick a operation from the line above: ")
    b = float(input("Whats is the second number? "))
    
    calculation = operators[operation]
    first_answer = calculation(a,b)
    
    print(f"{a} {operation} {b} = {first_answer}")
    
    if input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to start a new one.: ").lower() == 'y':
      a = first_answer
    else:
      finished = True
      calculator()


calculator()


  



