def sum(x:int,y:int)->int:
    if isinstance(x,int) and isinstance(y,int):
        return x+y 
    else: 
        print("Error ")

print(sum("mina","ahmed"))
#==============================================#
# FASTAPI  ===> Web Framwork
#===============================================#

def sayhello():
    print("Hello Mina")

sayhello()


#============================================#


def sum(x,y):
    print("Call Sum 2 Argument ")
    return x+y


def sum(x=0,y=0,z=0):
    print("Call Sum 3 Argument ")
    return x+y+z

print(sum(1,2))  #3 
print(sum(1,2,3)) #6
print(sum(1)) #6


'''
def Minarange(start,end=None,step=1): 
    if end == None : 
        end =start 
        start=0
    ...
    ....
    ....
'''

def add_items(item,l=[]):
    l.append(item)
    return l

list1=add_items("mina") #["mina"]
print(f"{list1}")
list2=add_items("ahmed") # ["mina",ahmed] 
print(f"{list2}")

def add_items(item,l=None):
    if l == None :
        l=[] #New Location
    
    l.append(item) 
    return l

list1=add_items("mina") #["mina"]
print(f"{list1}")
list2=add_items("ahmed") # [,ahmed] 
print(f"{list2}")




import random

def choise_random (rand=random.choice([1,2,3])):
    return rand


def choise_random (rand=None):
    if rand == None:
        rand=random.choice([1,2,3])
    return rand
print(choise_random())
print(choise_random())
print(choise_random())
print(choise_random())


#===============================================#

# calling using Positional Argument 
# func(l,True)
# calling using Keyword Argument 
# func(data=l,reverse=True)
def sum(x,y):
    print(f" {x=}  {y=}")
    return x+y
#sum=5
print(sum(15,10))
print(sum(x=5,y=10))
print(sum(y=10,x=5))

def sum(x,y,z):
    print(f" {x=}  {y=} {z=}")
    return x+y+z

# print(sum(x=10,5,6))
print(sum(10,z=5,y=6))
# print(sum(10,x=5,y=6)) Type Error : multiple values for argument 'x'



def say_welcome (**data):
    print(data)
    for key,value in data.items():
        print(f" {key} {value}")

dict1={
     "name":"mina",
     "age":30
}
dict2={
     "name":"ahmed",
     "age":30,
     "salary":3000
}
#dict1.update(dict2)
#print(dict1)
#set=set()
dict3={**dict1,**dict2}
print(dict3)
# print(**dict)
say_welcome(name="mina",age=30,salary=30000)
say_welcome(**dict1)






def say_hello(name,age,salary):
    print("Say Hello ",name,age,salary)


dict={
    "name":"mina",
    "age":30,
    "salary":30000
}

say_hello(**dict)


'''
    name="mina","age"=30 == ** ==> dict 
    dict == ** ==> name="mina","age"=30
    1,2,3,4 === * ===> Tuple 
    Tuple ====* ==> 1,2,3,4
'''

def sum(*data):
    print(data)
    #sum(data)
    sum1=0
    for i in data :
        sum1+=i
    print(sum1)


sum(5,5,50,20,30,100,50,10) #210


def function (*args , **kwargs):
    pass 


#======================================
# Pythonn How to Pass ? 
# ==========================

def say_welcome(x):
    print(f"Inside Function Before Increment : {id(x)}")
    x+=1
    print(f"Inside Function After Increment : {id(x)}")
    print("Inside Function : ",x) 


x=5 
print(f"Outside Function id : {id(x)}")
print("Outside  Function  Before call : ",x) 
say_welcome(x)
print("Outside  Function  After call : ",x) 


print("========Pass Mutable object =====")
def say_welcome(lst):
    print(f"Inside Function Before Append : {id(lst)}")
    lst.append(1)
    print(f"Inside Function After Append : {id(lst)}")
    print("Inside Function : ",lst) 


lst=[5]
print(f"Outside Function id : {id(lst)}")
print("Outside  Function  Before call : ",lst) 
say_welcome(lst)
print("Outside  Function  After call : ",lst) 

#==================Scope===================#
# Python follows the LEGB rule to resolve variable names:
# L (Local): Inside the current function.
# E (Enclosing): In enclosing functions (for nested functions).
# G (Global): At the top level of the module or script.
# B (Built-in): In the built-in names (e.g., print, len).

x=10 #Global 

def test():
    global x
    print(f"Function Before change {x=}")#10
    x=20
    print(f"Function After change {x=}")#20

print(f"Globla Before call {x=}")#10
test()
print(f"Globla After call {x=}")#20

x=10
def test():
    #print(f"Function Before change {x=}")#Error
    x=20
    print(f"Function After change {x=}")#20

print(f"Globla Before call {x=}")#10
test()
print(f"Globla After call {x=}")#10


# ===================================

x=10
def test():
    a=10 #Local test  #Enclosing Test2
    print("Print test:" ,a) #10
    def test2():
        # print("Print test2 Before change:" ,a) #Error
        a=20 #Local 
        print("Print test2: After change:" ,a) #20
    test2()
    print("Print test:" ,a) #10 

print("="*10)
test()
# ===================================

x=10
def test():
    a=10 #Local test  #Enclosing Test2
    print("Print test:" ,a) #10 
    def test2():
        nonlocal a #test2 don't have a local  
        print("Print test2 Before change:" ,a) #10
        a=20 #Enclosing Test2 
        print("Print test2: After change:" ,a)#20 
    test2()
    print("Print test:" ,a) #20 

print("="*10)
test()
# ========================================


def mulitply_double(number):
    return number*2

def mulitply_triple(number):
    return number*3

def mulitply(mult):
    return lambda number : number*mult

# def mulitply_triple(number):
#     def multiply (mult):
#         return number*mult 
#     return mulitply



double=mulitply(2)
triple=mulitply(3)
print(type(double))
print(mulitply(5)(2))
print(double(5)) #5*2 
print(triple(5)) #5*3
# ========================================

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
}

print(operations["add"](2,5))
print(operations["subtract"](2,5))
print(operations["multiply"](2,5))

# ========================================

def double(x):
    return x*2
def even(x):
    if x%2==0:
        return x

# l=list(map(double,[12,15,30]))
l=list(map(lambda x : x*2,[12,15,30]))
print(l)
#lambda arguments: expression if condition else expression
# l=list(filter(even,[12,15,30]))
l=list(filter(lambda x: (x%2==0) and x,[12,15,30]))
l=list(filter(lambda x: x if x%2==0 else None,[12,15,30]))
print(l)


l=[1,2,3,4]
result=map(lambda e:e*2,filter(lambda e:e if e%2==0 else None,l))
print(list(result))

import time 
def decrator_say_hello(function):
    def wrapper(*args,**kwargs):
        print("Hello We Love Linux and eng.Mina")
        function(*args,**kwargs) #calling
        print("Good By We Hate Windows & Node JS  ")
    return wrapper

def decratortime(function):
    def wrapper(*args,**kwargs):
        print("Before Call Function")
        start=time.time()
        function(*args,**kwargs) #calling
        print("After Call Function ")
        end=time.time()-start
        print(f"This function take : {end} sec")
    return wrapper


# decratortime(test)()
@decrator_say_hello
@decratortime
def test(z):
    for i in range(1,10000000):
        pass 

test(5)
#@decratortime
def test2():
    for i in range(1,10000000):
        pass 

test2()





