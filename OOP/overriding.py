class A:
    def show(self):
        print('a show from A')


class B(A):

    #here even the parent has show method the child class overrides it 
    def show(self):
        print('Show from B')



obj1=B()
obj1.show()