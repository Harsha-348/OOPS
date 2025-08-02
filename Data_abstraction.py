# Data Abstraction

from abc import ABC,abstractmethod

#Abstract class
class Animal:

  @abstractmethod
  def sound(self):
    pass
  def eat(self):
    pass

#Concrete class
class dog(Animal):
  def sound(self):
    return "dog barks"
  def eat(self):
    return "dog eats"


dog1 = Dog()
print(dog1.eat())
print(dog1.sound())
