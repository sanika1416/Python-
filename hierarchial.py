class pets:
    def speak(self):
        print("the animal speaks")
        
class Dog(pets):
    def bark(self):
        print("the dog barks")
        
class Cat(pets):
    def mew(self):
        print("the cat mews")
        
dog=Dog()
cat=Cat()

dog.bark()
cat.mew()