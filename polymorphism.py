# Compile time (Method Overloading)

class calculator:
  def add(self,a,b = 0,c = 0):
    return a + b + c

calc1 = calculator()
print(cal1.add(3,1))
print(cac1.add(2,4,6))
    
# Run time (Method Overriding)

class animal:
  def speak(self):
    return "animal makes sound"

class dog:
  def speak(self):
    return "dod barks"

class cat:
  def speak(self):
    return "cat meows"

animals = [animal(),dog(),cat()]

for animal in animals:
  print(animal.speak())
