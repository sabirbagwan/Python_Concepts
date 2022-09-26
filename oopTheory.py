"""
    # Constructor : It is a special kind method (function of a class) inside a class, of which code is automatically gets excecuted as
    # soon as an Object of that class is created.

    ## Self is basically the currunt object

SELF == Self is an argument which is passed by Python everytime a 


putting dundurscore (double underscore before a variable in class makes it private)(though by get and set function you can give control
 of it) because in Python there is nothing called as hiding the variables entirely like java
pin becomes __pin 

Instance variable is a variable whos value is different for different instances.. like in ATM class example
the value of pin is different for every custer ( it is defined inside the constructor)
we can access instance variable by self. ()
vs
Static/class variables is a variable whos value is same for all the instances (is is defined outside the constructor) 
we can access the class variables by atm.   ## by calling class name 

If you are creating a method using static variables then it is called as static method and 
@staticmethod is used to show it and 'self' is not needed to access them


RELATIONSHIP 
1. Aggregation ( has - a) like (customer has a address)
2. Inheritance ( is - a ) like (smartphone is a product / car is a vehicle)

Inheritance gives code reusability

decorators are functions which are executed before your function/methods

Polymorphism
1. Method Overriding
2. Method Overloading
3. Operator Overloading


lambda input: expression