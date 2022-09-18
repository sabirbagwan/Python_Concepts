## Single Level Inheritance

class Father():
    def python_lover(self):
        print('I love to code in Python')

class Child(Father):
    def golang_lover(self):
        print('I love to code in Golang')

c = Child()
c.python_lover()
c.golang_lover()

# --Output--

# I love to code in Python
# I love to code in Golang
