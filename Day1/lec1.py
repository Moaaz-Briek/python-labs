# Scripiting File  (Magic Line )
    # #! /usr/bin/python3
    # print("hello cloud")
# VS Code     Vs    IDE  
# VS Code ----> Code Editor 
# Integred Development Enviroment --> Tools One APP ---> Specific 

# Python Language  
# C , C++ , JS , Node
# ============================================================================================
# File1.c 
# file1.h    ---> Preprocess --> File1.i ---> Compiler ---> File1.o ---> Linker ----> File.exe
# File2.c                        File2.i                    File2.o        |
# file2.h                                                                library
# Static Link 
    # High Code Size 
    # more Speed , more Safe Runtime 

# #define Winodws 1
# # define OS Winodws
# # if OS == Windows 
#     code Windoes 
# # else 
#     code Linux 


# Code[Windows] ===> ToolChain[Windows] ----> File.exe
# Code[Linux] ===> ToolChain[Linux] ----> File
# Code[AVR] ===> ToolChain [AVR] ===> file.hex


# ============================================================================================
# APP ====> OS   =====> HW 
# APP ====> JVM ====> OS =====> HW
#============================================================================================
# Code [Java] ===> Compiler [Java C] ==> ByteCode 
# ByteCode
# JVM [Library]
# OS [Windows - Linux -MAC]

# Write Once Run any Where 
# Dynamic Linking 
# Java Fully Compiler VS Fully Interperter
# ============================================================================================
#  Compiler                      vs                       Interperter 
#  President Arabic === Check Syntax[Translator]  ===> One Paper (English) ===> Speak 
#  Source Code      === Compiler ====> Exectuable ===> Run

# koler  ==== Translator [Translate on the Fly] [JIT:Notes]===> speak 
# source Code ==== Interperter ====> Run

# JIT ===> Just in Timer  ==> Mentor LOOPing 
#============================================================================================
# Python ====> Compiler VS Interpter ?
# ======================================
# print("Hello")
# if True 
#     print("Mina")

# print("Hello")
# print(5+"5") #Error 

# Python ====> TOOLCHAIN ===> Run 

# Python ===> Cpython [ Default ] ===> Run 
# Python ===> jython ===> Run
# Python ===> PyPy ===> Run
# Python ===> MicroPython ===> RUn
#============================================================================================
# GIL  #Global Inperter Lock 
# X ==> iron Python 
# X ==> Jython 
# CPython ===> C  ==> Slow  [Official]
# PyPy   ==> Fast 
# Micropython ==> Fast 
#===========================================================================================
# PYPY ===> Large Memory usage than Cpython 
# 2-10 x Faster Execution than Cpython 
#============================================================================================
# Python  :- 
# =============
    # Type Language 
            # Static VS Dynamic Language 
            #==============================
            # Static Language 
            # 1- Define DataType Variable Before Run & Compiler 
            # int x=5; 
            # 2- Can't change type of Variable in Run Time 
            # x="mina";     
            #error: invalid conversion from 'const char*' to 'int' 

            #Dynamic language (Js , Python )
                # 1- Define DataType Variable in Running  
                # 2- Can Change DataType  for Variable in Running  
	            #var x=5
	            #x="mina"
              #Python 
                # x=5
                # print(type(x)) #class<int>
                # x="mina"
                # print(type(x)) #class<str>

            # Strong VS weak 
                # Weak  , Lessely ---> Allow Automatic Casting [Convet Datatype to Aother Automatic ]
                    # console.log("5"+6) #56
                    # Js Automatic casting 6(int) --> "6" (string) [Concate]
                     # if (5 == "5") {
                     # console.log("Ok")  
                     # }
                    # if (5 === "5") {
                    # console.log("Ok")  
                    # }
                # Strong   ---> don't allow Automatic Casting [Convet Datatype to Aother Automatic ]
                   # print(str(5)+"6")
	               # print(5+"6") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
                   # print("="*3)  Notes : string * Number ---> Valid - string + Number --> Not Valid 

    # Paradigms Supported  
'''
    Imperative Paradigms  : Structure Paradigms
    def employee(name,salary):
        print("employee")
        print("Employee Name : ",name )
    def main(name,salary): 
        print("call  main")
        employee(name,salary)
    main("mina",30000)
'''

'''
Imperative Paradigms  : OOP Paradigms
class Employee():
    def __init__(self,name,salary): 
        self.__name=name
        self.__salary=salary
        print("employee")
        print("Employee Name : ",name )
        print("Employee Salary : ",salary )
        e=Employee("mina",5000)

'''
'''
Declartive Paradigms  : Functional Paradigms
    l=[1,2,3,4]
    string=list(map(str,l))
    print(string)
'''
            
    # Memory Management 
         #  Fully Manula Control [C-C++]
            # Memory Leak 
            # Holes  
         #  Automatic Control Memory [Garbage Collector] 
            # java 
            # Python 
         # Manual - Autmotic 
            # Rust - OwnerShip - Control Memory 
            # Modern C++  - Smart Pointer - Pervent Memoy Leak    


#REPL  ===> Read Evaluate Print LOOP 

#======================================== Python ================================================#

# Variable : Named Location  [Reference] in Memory used to store data 

# Data Types :
    # Simple 
            # Number (int  , float), string ,boolean , None 
    #Containers 
            # List   - Dict - Tuple - Set 

# Immutable Object  : Change on Place 
# Mutable Object : Can't Change On Place 

# Integers [Immutable ] 
x=1
print(id(x))  #.......... 225
x=2
print(id(x)) #............256

print("="*50)

# Single Line Comment # 
# Multi Line Comment [ ''' ''' ] [""" """]
"""
x=5
y=5
print("id(x)" , id(x)) 
print("id(y)", id(y)) 
y=y+1 #6
x=x+1 #6
print("id(x)" , id(x)) 
print("id(y)", id(y)) 
"""

# x=0 
# y=0 
# while id(x)==id(y):
#     x=x+1 
#     y=y+1 

# print(x,y)

x=300 
y=300 
print(id(x)==id(y)) #True 
print(x is y) #True 
print("id(x)" , id(x)) 
print("id(y)", id(y)) 
x=x+1 #301
y=y+1 #301
print(id(x)==id(y)) #False 
print(x is y) #Fasle
print("id(x)" , id(x)) 
print("id(y)", id(y)) 


# Operators ==> + - / % //(Integer Division ) 



#==================================================================================================#
print("="*50)
print("string Example")
x="mina"
y="mina"
print("id(x)" , id(x)) 
print("id(y)", id(y))
x=x+"s" #minas
y=y+"s" #minas
print("id(x)" , id(x)) 
print("id(y)", id(y))

# >>> 10/5
# 2.0
# >>> 9/5
# 1.8
# >>> 9//5
# 1
# >>> -9/5
# -1.8
# >>> -9//5
# -2
# floor

#x%3==0 and x%5 ==0  ===> x%15==0
# > , < , == , <= ,<=
#Check Integers can't is check [Reference] , == 
# Lesson Learn : Don't Use Referece Check [is] with Integers 
#==================================================================================================#
# Floating ===> IEEE754
x=0.2 
y=0.1
print(x+y) 
print((x+y)==0.3) #False
print(round((x+y),2)==0.3) #True
#==================================================================================================#
# Boolean DataType 
x=True 
y=True 
print(x is y) #True 
x=False 
print(x is y) #False 
#==================================================================================================#
# String 
# print("mina"+5) #TypeError: can only concatenate str (not "int") to str
# print("mina" + str(5))
# str="mina" 
# print("mina"+str(5)) #TypeError: 'str' object is not callable

# number_of_student=

# Build in Function ===> Reserved Keyword
# if while break continue pass def 
#==================================================================================================#
# Can't Print Different Variable in print
# How Fix Problem 
f_name="mina"
l_name="nagy"
age=32 
# COnvert 
print("My name is "+f_name + " " + l_name + "age = "+ str( age) )
# Comma 
print("My name is ",f_name," ",l_name," age = ",age , sep='')
# print("Mina Loves Linux", "Python",sep=" & ")
# print(" cloud  ",end=" ## ")
# print(" Geeks ")
# %  Older Style
print("My name is %s My age = %d " %(f_name+l_name,age) )
# String Format 
print("My name is {} {} My age = {}".format(f_name , l_name ,age ))
print("My name is {1} {0} My age = {2}".format(f_name , l_name ,age ))
print("My name is {n} {l} My age = {a}".format(n=f_name , l=l_name ,a=age ))

# print("My name is {} {} My age = {}".format(f_name , l_name )) #Error 

#f-format - ----> 3.6 
print(f"My name is {f_name} {l_name} My age = {age}")
print(f"{f_name=}")  # print(f"f_name={f_name}") # f_name = value 
print(f"{id(f_name)=}") # print(f"f_name={f_name}")  #id(f_name)= .....
# =================================================================================
# String ===> Immutable  ==> " " ' ' 
name='mina' #name="mina" 
#String Access By index  0 , length -1 
print(name[0])  # m 
# name[0]='a' #Immutable ==> Change Object in Same Place  [TypeError: 'str' object does not support item assignment]
print(f"{id(name)}")
name="Ahme"
print(f"{id(name)}")
#=============================================================
# Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
print(type(c)) #str
#=============================================================
# Slicing
name="Hello Mina Nagy and Cloud we Love Linux and Hate Windows" 
print(name[:8]) #index 0 ---> 7  #Hello Mi
print(name[:8:2]) #index 0 ---> 7 --> 0 2 4 6 -->  #HloM
print(name[-1]) #index -1 ==> Last Character ===>S
print(name[15:3:-1]) # index 15 : 4 ==> 15 , 14 ,13 ,.......5,4
print(name[15:3:-2]) # index 15 : 4 ==> 15 , 13 ,11 ,.......6,4
print(name[::-1]) 
#=============================================================
x="yoyo" #===> "oyoy"
print(x==x[::-1]) #False
x="goog" #===> "gogo"
print(x==x[::-1]) #True 
#=============================================================
name="mina"
print(f"{id(name)}")
# name[0]='s' ==> Error 
name='s'+name[1:] #'s'+"ina"
print(name) #sina
print(f"{id(name)}")
#=============================================================
name="Hello Mina Nagy and Cloud we Love Linux and Hate Windows" 
print(len(name))
print(name.find('linux')) #Not Found ==> -1
# print(name.index('linux')) #Not Found ==> ValueError

# print(name.replace('Linux','Python')) 
new_string=name.replace('Linux','Python').upper()
print(new_string) 
# Method Chaining [Immutable] 
    # string.function().upper()
    # None.upper()
# name=name.replace('Linux','Python')
print(name)
name="Hello-Mina-Nagy-and-Cloud-we-Love-Linux-and-Hate-Windows" 
print(name.split(' '))

print('linux' in name.lower() ) #memebership
print(name.lower().count('l'))#5

string=" Hello \n \
Mina \n \
Nagy"
print(string)
string=""" Hello 
Mina 
Nagy 
"""
print(string)
string='''
Hello 
Mina 
Nagy 
''' 

print(string)
#=============================================================
