# Core Concept OOP
    # Class 
    # Object 
    # Attributes 
        # Instance Attributes 
        # Class Attributes 
    # Consturctor 
    # Methods # Behaviour Object 
       # Class Method : #Class 
       # Instance Method : #Belond Object 


# Key OOP 
    # Encapsulation 
    # Inherintace 
    # Ployohism 
    # Abstraction 


#Class ==> New Data Type [Blue Print] for creation Object [Variable]
class Employee:
    #class Attribute
    names=[] #classAttribute
    #...
    # def __new__(this):
    #     print("Create Object")
    # Instance Attributes  
    def __init__(this,name=None,age=None,salary=None,email=None): #Constructor 
        print("Call Contructor for initalization Object")
        this.__name=name 
        this.__age=age 
        this.__salary=salary
        this.__email=email
        #Employee.names.append(name)
        this.__class__.names.append(name)

    @property
    def age(this):
        return this.__age
    @age.setter 
    def age(this,age):
        if age>0 and age <100 : 
             this.__age=age 
        else : 
            print("Error in Age Value ") 


    @property
    def name(this):
        return this.__name
    
    @name.setter 
    def name(this,name):
        if len(name) > 5 : 
             this.__name=name 
        else : 
            print("Error in name Value ") 

    '''
        def set_name(this,name):
            pass
        def get_name(this):
            pass 
        name=property(set_name,get_name)
    '''

    #@classmethod
    #def allname(cls):
        #return cls.names
    @property
    def allname(this):
        return this.__class__.names
    @staticmethod
    def validate_email(email): #Helper Method
        if "@" in email and '.' in email:
            #print("Valid Email ")
            return 1
        else : 
            # print("Not Valid Email ")
            return 0
    @property
    def email(this):
        return this.__email
    @email.setter 
    def email(this,email):
       # if "@" in email and '.' in email:
            # this.__email=email 
       # else : 
          #  print("Error in Email Value ") 
        if Employee.validate_email(email):
            this.__email=email 
        else : 
            print("Error in Email Value ") 

    # def set_age(this,age): 
    #    if age>0 and age <100 : 
    #         this.__age=age
    #    else : 
    #        print("Error in Age Value ")  
    # def get_age(this):
    #     return this.__age 

    def work(this):
        pass 
    # __ func__ ==> Dunder Function or Magic Function
    def __str__(this):
        return f"Employe(name,age,salary,email) =({this.__name},{this.__age},{this.__salary},{this.__email}) "
    def __repr__(this):
        return f"Employe(name,age,salary,email) =({this.__name},{this.__age},{this.__salary},{this.__email}) "
    def __add__(this,other):
        name=this.__name+other.__name 
        age=this.__age+other.__age 
        salary=this.__salary+other.__salary 
        email=None
        return Employee(name,age,salary,email)
    # def __iter__ ():
    # def __gt__():
    # def __lt__():
        

# Node [Mongo] ===> Mongosse [ODM] ===> DB 
# Python + OOP ===> ORM [Object Relational Mapping]  SQLAlchamy ===> DB(SQL)
# Class       ====> ORM ===> Table 
# Object      ====> ORM ===> ROW 


#Create Object  
e= Employee("mina",30,30000,'mina@gmail.com') 
e1= Employee("Ali",30,30000,'Ali@gmail.com') 
e2= Employee("Ahmed",30,30000,'Ahmed@gmail.com') 
e3=e+e1
print(e3) #<__main__.Employee object at 0x775784817bb0>
# if Employee.validate_email('Ahmed@gmailcom'):
#     e1.email='Ahmed@gmailcom'
# else :
#     ...

# print(type(e))
print(Employee.allname)
#AttributeError: 'Employee' object has no attribute 'name'
# print(f'{e.name}') #error 
# print(f'{e.age}') #error 
# print(f'{e.salary}')# error 
# print(f'{e._Employee__name}') # 
# print(f'{e._Employee__age}') # 
# print(f'{e._Employee__salary}')#  
# e.name="Ali"
# e.age=-5 
# e.salary=-20 
# print(f'{e.name}')
# print(f'{e.age}')
# print(f'{e.salary}')
# print(e.get_age())
# e.set_age(20)
# print(e.get_age())
print(e.age)
e.age=-25 
print(e.age)



# Constructor ===> Special Methods ==> Intialization Object 

#inherintance 
from abc import ABC ,abstractmethod
class Animal(ABC): #Abstract Class 
    def __init__(self,name,color):
         print("Constructor Animal ")
         self.__name=name 
         self.__color=color

    @abstractmethod    
    def sound(self):
        print("Animal Sound")


class Dog(Animal): 
    def __init__(self,name,color,type):
        print("Constructor Dog ")
        super().__init__(name,color)
        self.__type=type
    def sound(self): #Overriding 
        super().sound()
        print("Haw ....")

class Cat(Animal): 
    def __init__(self,name,color,type):
        print("Constructor Dog ")
        super().__init__(name,color)
        self.__type=type
    def sound(self):
        super().sound()
        print("Naw ....")

animal=[Dog("Lucky","White","Balady"),Cat("Nono","black","Balady")]#,Animal("test","gray")]
# print(type(animal))
#animal[0].sound()
#animal[1].sound()
#animal[2].sound()
for i in animal:
    i.sound() # sound --> on Every 

class Person():
    def __init__(self,name,color):
         print("Constructor Animal ")
         self.__name=name 
         self.__color=color
    def sound(self):
        print("Person Sound")

def makeSound(thing):
    thing.sound()

p=Person("mina","Black")

makeSound(p)
makeSound(animal[0])
makeSound(animal[1])
# makeSound(animal[2])

def add(x,y):
    print(x+y) 

add(2,3) #5
add("Ahmed","Ali") #Ahmed + Ali 


# Polymorphism in Python 
# Duck Typing 
# Overloading Operator 
# Method Overriding
# Method Oveloading [Not Direct using Default value or * args **kwargs] 

# Python ==> Interface ===> Multi Inherinatance 



