class grandparent:
    def greet(self):
        print("hello from grandparent")
        
class parent(grandparent):
    def hello(self):
        print("hello from parent")
        
class child(parent):
    def introduce(self):
        print("hello from child")
        
family=child()
family.greet()
family.hello()
family.introduce()