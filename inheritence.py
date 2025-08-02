# ------------- ( Single inheritence) ---------------

class person:
  def __init__(self,name):
    self.name = name

class employee(person):
  def __init__(self,name,salary):
    super().__init__(name)
    self.salary = salary
    
emp1 = employee("john",500) 
print("name:",emp1.name,"| salary:",emp1.salary)

# ------------- ( Multiple inheritence) ---------------

class job:
  def __init__(self,salary):
    self.salary = salary

class multiroleemployee(employee,job):
  def __init__(self,name,salary):
    employee.__init__(self,name,salary)
    job.__init__(self,salary)

emp2 = multiroleemployee("don",200)
print("name:",emp2.name,"| salary:",emp2.salary)

# ------------- ( Multi-level inheritence) ---------------

class manager(multiroleemployee):
  def __init__(self,name,salary,department):
    multiroleemployee.__init__(self,name,salary)
    self.department = department

emp3 = manager("jack",700,"hr")
print("name",emp3.name,"| salary",emp3.salary,"|department",emp3.department)

# ------------- ( Hierarchical inheritence) --------------

class assistantmanager(multiroleemployee):
  def __init__(self,name,salary,department,team_size):
    multiroleemployee.__init__(self,name,salary)
    self.department = department
    self.team_size = team_size

emp4 = assistantmanager("rose",400,"developer",5)
print("name",emp4.name,"| salary",emp4.salary,"| department",emp4.department,"| team_size",emp4.team_size)

# ------------- ( Hierarchical inheritence) --------------

class seniormanager(manager,assistantmanager): # it holds multiple inhertence and Hierarchical inhertence
  def __init__(self,name,salary,department,team_size):
    manager.__init__(self,name,salary,department)
    assistantmanager.__init__(self,name,salary,department,team_size)
'''
(or) --> "to remove duplicacy occuring use below one"
class seniormanager(manager,assistantmanager): # it holds multiple inhertence and Hierarchical inhertence
  def __init__(self,name,salary,department,team_size):
    super().__init__(name,salary,department)
    self.team_size = team_size
'''
emp5 = seniormanager("rose",20000,"head",5)
print("name",emp5.name,"| salary",emp5.salary,"| department",emp5.department,"| team_size",emp5.team_size)


    




  
