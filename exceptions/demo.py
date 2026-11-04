
# Exceptions are needed to handled the errors and gives the type of error to be handled every try should have atleat one except or finally block here if everything is right the try block executes and if something is wrong it goes to except block and finally excutes no matter which block is excuted

print('opened the resource')
try:
    a=int(input("Enter the Numerator"))
    b=int(input("enter Enter the Denominator"))
    result=a/b
    print(result)
except ZeroDivisionError as ze:
    print('Not divisible by zero',ze)
except ValueError as ve:
    print('enter the valid number',ve)
finally:
    print('the resources has been closed')

