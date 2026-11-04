
#abstraction: it has interfaces in it and can be implemented by other class in abstract class there should not be implemented and we cannopt create object of abstract class

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    def show(self):
        print('interface is implemented')


obj1=B()
obj1.show()


class paymentgateway(ABC):
    @abstractmethod
    def pay(self):
        pass
    

# so here in the example in order to use the razorpay or paypal they have to implement the abstract method from the paymentgateway class in order to make the classes to restrit to have pay method or implement the abstract method
class razorpay(paymentgateway):
    def pay(self):
        print('paying using razor pay')

class paypal(paymentgateway):
    def pay(self):
        print('paying using paypal pay')


class Purchase:

    def __init__(self,gateway):
        self.gateway=gateway
    def checkout(self):
        print("checking out...")
        self.gateway.pay()


gateway1=razorpay()
purchase=Purchase(gateway1)
purchase.gateway.pay()