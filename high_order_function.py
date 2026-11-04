#High Order function is nothing but function that takes other function as a parameter

def square(num):
    return num*num

def cube(num):
    return num*num*num

def operate(num, operator):   # this function is called higher order function it takes another function square or cube as parameter
    return operator(num)

print(operate(5,cube))
