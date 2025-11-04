class Animal:
    def speak(self):
        print("animal speaks")
    
class Dog(Animal):
    def bark(self):
        print("dog barks")
    
dog=Dog()
dog.speak()
dog.bark()