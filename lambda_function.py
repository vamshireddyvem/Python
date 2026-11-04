# a function that can be used once it is an anonymus function



from functools import reduce


result=lambda a,b:a+b

print(result(3,4))

#filter: it filters and it takes the condition/funtion and iterable
nums=[1,2,3,4,5,6,7,8,9]
evens=[]

evens=list(filter(lambda n:n%2==0,nums))
print(evens)

#map: it iterates whole iterable
doubles=list(map(lambda n:n*2,nums))
print(doubles)

#reduce: it is an functools module where can reduce the iterable using the condition/function

sum=reduce(lambda a,b:a+b,nums)
print(sum)