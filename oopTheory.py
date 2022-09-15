"""
    # Constructor : It is a special kind method (function of a class) inside a class, of which code is automatically gets excecuted as
    # soon as an Object of that class is created.

    ## Self is basically the currunt object

putting dundurscore (double underscore before a variable in class makes it private)(though by get and set function you can give control
 of it) because in Python there is nothing called as hiding the variables entirely like java
pin becomes __pin 

Instance variable is a variable whos value is different for different instances.. like in ATM class example
the value of pin is different for every custer ( it is defined inside the constructor)
we can access instance variable by self. ()
vs
Static/class variables is a variable whos value is same for all the instances (is is defined outside the constructor) 
we can access the class variables by atm.   ## by calling class name 