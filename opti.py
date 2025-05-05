import gurobipy

print("ici c'est la branche de antoine")

# create a function that gives the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)