# one method having differnt behaviours it means poly: many morphism: behaviors
# this can be achieved in three ways
#1: Duck typing: a python treats everything as a Duck as long it Quacks like a duck
#2: Operands Overloading: it is a same method but behaves differnt based on the Operands
#3: Method Overriding : it is a method where it overrides the method and behaves different


class Laptop:
    def build(self):
        print('laptop builds')


class desktop:
    def build(self):
        print('desktop builds')

# here we are passing the laptop but still uses desktop because of ducktyping here as long as the class has a quack method like build here it behaving like that class since while calling the build we have used desktop object apple and it works because of desktop
class Programmer:
    def build(self, machine:Laptop):
        print('Programmer coding')
        machine.build()

dell= Laptop()
apple=desktop()
nani=Programmer()
nani.build(apple)
