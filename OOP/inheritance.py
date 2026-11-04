
## this is Multi-Level Inheritance

class A:
    
    def __init__(self):
        print('this is class A init')

    def f1(self):
        print('this is function f1 from class A')

class B(A):
    def __init__(self):
        print('this is class B init')
        
    
    def f2(self):
        print('this is function f2 from class B')


class C(B):
    # def __init__(self):
    #     print('this is class C init')
    
    def f3(self):
            print('this is function f3 from class C')


class D:
    
    def __init__(self):
        print('this is class D init')

    def f4(self):
        print('this is function f4 from class D')

class E():
    def __init__(self):
        print('this is class E init')
        
    
    def f5(self):
        print('this is function f5 from class E')

# this is the mutliple Inheritance and it follows MOR (Method Order Resoloution); where it check it own class then the order of inheritance that is given
class F(E,D):
    # def __init__(self):
    #     print('this is class C init')
    
    def f6(self):
            print('this is function f6 from class F')

obj1=C()
obj1.f1()
obj1.f2()
obj1.f3()
obj2=F()
obj2.f6()