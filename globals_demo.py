a=10                #Global Variable

def num():

    print(globals()['a'])       # we can access the global variable using global() it returns a dict{k,v} pairs and we can target that global variable using key as 'a' and get the value of which in this case its 10
    a=15            #local variable
    print(a)

num()