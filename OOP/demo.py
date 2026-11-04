class Computer:
    #this brand is a class variable and can be accessed using class or object
    brand='dell'

    # def __new__(cls):
    #     print('this is a constructor')
    #       return Super(Computer,cls).__new__(cls)
        
    # by default all the methods are instance methods 
    def __init__(self,pr,st,me):
        self.pr=pr
        self.st=st
        self.me=me

    def config(self):
        print(f"config method ",self.pr)

    # this a class method where we use @classmethod as a decorator to make a mrhod as a class method and this method is takes class (cls as variable) as parameter
    @classmethod
    def info(cls):
        return Computer.brand

    # this is method which is used to for function that has to nothing with instance or a class it is just a UTI method where use for a particular operation and we can make this happen using static method and it can be done using @stasticmethod as a decorator
    @staticmethod
    def get_bytes(gb):
        return gb*(1024**3)


com1=Computer("i9",'512gb',16)
com1.config()

print(Computer.info()) # here we are calling the class method

print(Computer.get_bytes(16))