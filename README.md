# OOPS (Object Oriented Programming System) 

- It is a programming pattern that is designed to model real-world entities through classes and objects.
- In simple words, it allows developers to structure their code in a efficient,scalable and maintainable way.

# OOPS provides features (4-Pillars):
 - Inheritence
 - Polymorphism
 - Encapsulation
 - Data Abstraction

-------------------------------------------------( Class & Objects )--------------------------------------------

# (Class)
- A class is a collection of objects.
- It acts like a blue print for creating objects.
- It defines the attributes and methods that the objects can have.
- Class is creates using the keyword "Class".
- Attributes are nothing but variables and are accessable using (.) dot operator.

# (Object)
- It is an instance of a class.
- It is the actual implementation of the class.
- It consists of:
   - state: These are the attributes or variables that describe the object. ex: name,age
   - behavior: these are the methods that tell what object can do. ex: bark(),sleep()
   - identity : These are the variable names of the object, that are different from one another. ex: dog1,dog2
  

-------------------------------------------------( Inheritance )--------------------------------------------

# (Inheritence)
- It allows a class which is a "child class" to inherit all the properties and methods from another class which is a "Parent class".
- It supports Hierarchical classification and Code resuability.

Types of inheritence:
      - Single inhertence
      - Multiple inheritence
      - Multi-level inheritence
      - Hierarchical inheritence
      - Hybrid inheritence

1. Single inhertence:

 In single inheritence, A child class inherits from a single parent class.

2. Multiple inheritence:

In Multiple inheritence, A child class inherits from more than one parent class.

3. Multi-level inheritence:

In Multi-level inheritence, A child class inherits from a parent class which in-turn that parent class inherits from another class.

4. Hierarchical inheritence:

In Hierarchical inheritence, Multiple child classes are inherited from a single parent class.

5. Hybrid inheritence:

In Hybrid inheritence, There will a combination of two or more types of inheritence.

-------------------------------------------------( Polymorphism )--------------------------------------------

# (Polymorphism)
- It allows methods to have the same name but behave differently based on the objects context.
- It can be achieved through "method overloading" and "method overriding".

Types of Polymorphism:
      - Compile Time ()
      - Run time ()

1.  Compile Time:

- It is determined during the compilation of a proram.
- It allows methods to have the same name but behave differently based on the input parameters that are given.
- It is also reffered as method overloading.

Note: Technically, python doesn't support method over loading  but we can mimic it by using parameters or default arguements.
      It does method overloading because python does not allow methods to have the same name like C++ or Java.
      So, we use default arguements to mic and achieve over loading in python.

2. Run Time:

- It is determined during the run time of a program.
- It allows a sub-class to provide specific implementation of a method that is determined in it's parent class.
- It is also reffered as method overriding.

-------------------------------------------------( Encapsulation )--------------------------------------------

# (Encapsulation)
- It is a process of grouping methods and variable that operate on a data into a single unit,typically a class
- It restricts the direct access to the class components and protect the data.
- It can be achieved through public,private and protected.

1. Public member:
- It can be accessed from both inside or outside the class.
- They are the default members in python.

2. Private member:
- It is identified with a single underscore (_).
- It  can be accessed within the class or by the sub-class.

3. Protected member:
- It is identified with double underscore(__).
- It can be accessed from inside the class.

Note: If we want to access private and protected members of the class, Use getter and Setter methods:

- getter():

  It is used to access the values Private and Protected members of the the class.

- setter():

  It is used to modify the values of private and protected members of the class.

---------------------------------------------------( Data Abstraction )--------------------------------------------

# (Data Abstraction)
- It allows you to hide complex implementation details of the system and expose only the needed ones to the user.
- It helps you to focus on "what to do" and not "how to do".
- It can be achieved through abstract method, abstract class, concrete method and concrete class.

1. Abstract class:

It is a base class that defines the structure and is meant to be implemented.
It consists of all the abstract methods with only the structure and no real implementation in it.

2. Abstract method:

It is a method defined in the abstract class which has only structure and no real implementation in it.
it is filled by the concrete class

3. Concrete class:

It is a class in which all the concrete methods are defined with the real code implementation in it from the above super class.

4. Concrete method:

it is a method defined in the concrete class with the real code implementation in it.



---------------------------------------------------( Conclusion )--------------------------------------------

So, This is it !!

with all the conceptual explanation of OOPS and its four pillars in python.
You will get the code from the above .py files.
















