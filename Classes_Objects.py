# Class & Objects

# ------------------------------------------------------------( Class )----------------------------------------------------------------------

class dog:
  species = "canine"            # class attribute
  
  def __init__(self,name,age):
    self.name = name            # instance attribute
    self.age = age

# ------------------------------------------------------------( Objecta )----------------------------------------------------------------------

class dog:
  species = "canine"

  def __init__(self,name,age):
    self.name = name
    self.age = age

dog1 = dog("chintu",3)
dog1.name
dog1.age
dog1.species
