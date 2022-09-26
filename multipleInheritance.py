## Multiple Inheritance

class Father():
    def python_lover(self):
        print('I love to code in Python')

class Mother():
    def javascript_lover(self):
        print('I love to code in Js')

class Child(Father, Mother):
    def golang_lover(self):
        print('I love to code in Golang')

c = Child()
c.python_lover()
c.javascript_lover()
c.golang_lover()

# --Output--

# I love to code in Python
# I love to code in Js
# I love to code in Golang