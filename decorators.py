def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap

def sub(a,b):
    return a-b


#this is a decorator , it is a function where it take other function as parameter and return a function
# it has inner function where it does the necessary operations and return the operation and the decorator function returns the inner function to the calling function 

#modern way of calling the decorator function 
@greater_first
def divide(a,b):
    return a/b

#another way of calling the decorator function
sub=greater_first(sub)


print(divide(2,4))
print(sub(1,2))
