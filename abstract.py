from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class dog(animal):
    def sound(self):
       return "bark"
   
class cat(animal):
    def sound(self):
        return "meow"

d=dog()
c=cat()

print("dog sound: ",d.sound())
print("cat sound: ",c.sound())    
