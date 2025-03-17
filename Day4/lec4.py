'''
# Iterator vs Iterable 
# Iterable : Collection or container that can Be Iterator 
# Iterator : object that acutally performance iteration [for ....]


l=[1,2,3,4,5]
print(dir(l))
print("="*10)
string="Hello"
print(dir(string))
# str_iterator=string.__iter__()
str_iterator=iter(string)
#print(string.__next__())
print(type(str_iterator))
print(dir(str_iterator))
print(next(str_iterator))#H
print(next(str_iterator))#e
print(next(str_iterator))#l
print(next(str_iterator))#l
print(next(str_iterator))#o 
print(next(str_iterator))# Error # Stop Iterations
# print(str_iterator.__next__()) #H
# print(str_iterator.__next__()) #e 
# print(str_iterator.__next__()) #l
# print(str_iterator.__next__()) #l
# print(str_iterator.__next__()) #o
# print(str_iterator.__next__()) #Error  #StopIteration



def test(): 
    return 1  #Close[terminate] Execution Function dead Function 
    return 2 
    return 3


test() #1 
test() #1
test() #1
'''

# Generator 
# Special Type of Function return an iterator 
# Not use return yield 
# return ===> Single Value , yield ===> multi Value
def simple_generator(): 
    print("First call ")
    yield 1  #Pause Execution Function  
    print("Second call ")
    yield 2  #Pause Execution Function
    print("Third call ")
    yield 3  #Pause Execution Function


print(simple_generator()) #generator 
test=simple_generator()
print(type(test))
# print(next(test)) # First call  #1
# print(next(test)) # second call  #2
# print(next(test)) # Third call  #3
# print(next(test)) #StopIteration
for i in test: 
    print(i)
 
# Async VS Await ===> Co-routine   


# Python - List Comprehension
# Python - Dictionary Comprehension



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# l=[1,-2,-3,5,6]
# # [expression loop condition]
# # [Texpression if cond else Fexpression loop ]
# newlist=[x for x in l if x>0 ]
# print(newlist)
# nl = [x if x > 0 else 0 for x in l]
# print(nl)


def my_own_range(start,end=None):
    if end == None : 
        end=start #5
        start=0
    while start < end : 
        yield start  #0 #pause  #1 pause #2 Pause
        start+=1


l =[ i for i in range(1000000)]
# print(l)
import sys 
print(sys.getsizeof(l))
list_iterator=my_own_range(1000000)
print(sys.getsizeof(list_iterator))
next(list_iterator) #0
next(list_iterator) #1
next(list_iterator) #2
next(list_iterator) #3
# print(list(list_iterator))
#================ Files Importing =================
# import Data.devops as dev
# # Data.devops.test("Ahmed")
# dev.test("Ahmed")
# dev.test2("Ahmed",30)

from Data.devops import test,test2
test("Ahmed")
test2("Ahmed",30)