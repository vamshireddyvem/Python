#this is a function with arguments
def add(num1, num2):
    return num1+num2
print(add(1,3))

# This function is with default arguments, we can give a default value to a arguments in a function
#default arguments function
def sub(num1=0,num2=0):
    return num1-num2
print(sub(1))

# Variable Length Arguments function
# by this we can pass n no of arguments at the same time without specifying it before it takes the first one as a argument and from the second to end it takes the remainging arguments as tuple()
def mul(num1,*num2):
    for n in num2:
        num1*=n
    return num1
print (mul(1,3,4,5))

#keyword arguments
# this allows the function to use the arguments for proper type or order of arguments in a function
def person(name,age,loc):
    print("name : ",name)
    print("age : ", age)
    print("loc : ",loc)

print(person(28,'vamshi','dallas'))
#over here by by passing arguments without an order gives age as string(vamshi which is a name) so to solve this keyword arguments comes palce

print(person(loc='dallas',age=28,name='vamshi'))
#no matter the value of arguments get in to right place by using keyword arguments


#keyword variable length arguments, this is a type of function that allows both keyword and variale length arguments it stores the variable values?arguments from 2 to nth in form a dictonary {key:value} in key value pairs

def vamshi(education,**profession):
    print("education : ",education)
    for k,v in profession.items():
        print(k," : ",v)

print(vamshi(education='Docatorate',tech='java',tech2='node.js',tech3='python'))