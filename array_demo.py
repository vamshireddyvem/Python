from array import *

arr1= array('i',[])
i=1
while i<=6:
    data=int(input('enter the number '))
    arr1.append(data)
    i+=1

for n in arr1:
    print(n,end=""  )

arr2=(arr1.typecode,(n for n in arr1))
# Generator it gives a single list element in an array with a variable n and gives that variable(value) to a list that is using to store in new array for example here n is taking each value one by one and gives to the new array like arr2 here

arr3=(arr1.typecode,arr1.tolist())
#this tolist converts the arr1 into a list all together where it takes more memory as it has to take the copy of array 


print(arr2)
print(arr3)