class caluclator:

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b

    def divi(self,a,b):
        return a/b

c=caluclator()
result=c.add(int(input("enter a ")),int(input("enter b ")))
print(result)
print(c.divi(int(input("enter a ")),int(input("enter b "))))
