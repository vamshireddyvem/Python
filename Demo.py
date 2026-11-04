import math as m

from math import pow
numb=3

print(m.sqrt(numb))
print(pow(3,3))
names=['vamshi','Jinsu','maneesh', 'sai']
print(type(names))

nums=1,2,3,4,5,6
print(type(nums))

print(names[1])

order={1,3,5,7,8,9,2,3,6}
print(order)
print(type(order))

dict1={"vamshi":93345,"Jinsu":345689,"maneesh":1848598,"sai":12346}
print(dict1)
print(type(dict1))



x=10
y=15
x,y=y,x
print(x)


def student_details():
    student_name=input('Enter the Student Name ')
    student_Id=int(input('Enter student ID '))

    return print(f"Student name:{student_name}' \n 'and ID:{student_Id}")



num1=int(input("enter the value  "))

if num1%2==0:
    print(f'{num1} is a Even Number')
else:
    print(f'{num1} is a Odd Number')


