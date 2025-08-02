# Polymorphism

class Dog:
  def __init__(self,name,age,breed):
    self.name = name  # public 
    self._age = age   # protected
    self.__breed = breed # private

  def get__breed(self):   # getter method to access the attribute
    return self.__breed

  def set_age(self,age):  # setter method to modify
    if age > 0:
      self._age = age

dog1 = Dog("chintu",2,"canina")

print(dog1.name)
print(dog1._age)
print(dog1.get__breed())

dog1.set_age(5)
print(dog1._age)
