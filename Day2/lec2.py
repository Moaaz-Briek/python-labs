l=[1,2,3,5,"mina",'hello',3.5,None,True]
print(f"{id(l)=}")
l[0]="ahmed"
print(f"{l=}")
print(f"{id(l)=}")

# insert , append , extend 
l.append(20)
print(f"{l=}")
print(f"{id(l)=}")
l.extend([10,20,30,50])
print(f"{l=}")
print(f"{id(l)=}")
l.insert(2,"Cloud")
print(l)
#=====================================
l1=[1,2,3,4]
l2=[5,6,7]
l1=l1+l2
print(l1)
##=====================================
l=[1,2,3,5,"mina",'hello',3.5,None,True]
l.remove("mina") 
print(f"{l=}")
##=====================================
l=[1,2,3,5,"mina",'hello',3.5,None,True]
last=l.pop()
print(last)
print(l)
last=l.pop(2)
print(last)
print(l)
##=====================================
del l[0]
print(l)
##=====================================
l="m i n a".split(' ')
print(l)
##=====================================

l=['m','i','n','a']
string=' '.join(l)
print(type(string))

##=====================================
#Shallow Copy 
l=[1,2,3,4,5]
l1=l 
print(l==l1)
print(f" {id(l)==id(l1)}")





#import copy
from copy import copy,deepcopy
#Shallow Copy 
# l=[1,2,3,4,5]
# l1=l 
# print(l==l1)#True
# print(f" {id(l)==id(l1)}")#True

# #lc=l[::]
# #lc=l.copy() #copy Methods 
# #lc=copy.copy(l) # Copy Function
# lc=copy(l)
# print(l==lc) #True 
# print(f" {id(l)==id(lc)}") #False

#=====================================================
l=[1,2,3,[1,2,3],[0,2,0]]
lc=l[::]
lcd=deepcopy(l)
#=====================================================
l=[]
l=[0]*5 
print(l)
#=====================================================
l=[3,5,1,2,-1,-3]
print(l)
l=[3,5,1,2,-1,-3]
print(max(l))
print(sum(l))
#=====================================================
l=['Ahmed','Mina','Mariam','Hana']
l.sort(reverse=False,key=len)
# print(sorted(l,reverse=False,key=len))
# print(l)
#=====================================================
a,b=[1,2]

a=5 
b=6
a,b=[b,a]
a,_,b=[1,2,3]
a,*_,b=[1,2,3,4]
print(a,b)
a,*c,b=[1,2,3,4]
print(a,b,c)
#=====================================================

a=(1,2,3)
# a[0]=5
a=1,2,3
print(type(a))
a=1
print(type(a))
a=1,
print(type(a))
a=5 
b=6
a,b=b,a
a,_,b=1,2,3
a,*_,b=1,2,3,4
print(a,b)
a,*c,b=1,2,3,4
print(a,b,c)
#=====================================================
# Dictionary 
'''
dic={
    "key":value,
    "key":value,
    "key":value,
}
'''


employee={
    'name':'mina',
    'salary':30000,
    'name':'ali',
    'age':30
}
# print(employee)

# print(employee['name'])


# employee['name']='Ali'
# print(employee)

# del employee['salary']
# print(employee)

# print(employee.items())
# print(employee.values())
# print(employee.keys())
print("="*20)
for  key,value   in employee.items(): 
    print(key,value)
print("="*20)

for  value   in employee.values(): 
    print(value)

print("="*20)

for  key   in employee.keys(): 
    print(key)


print('name' in employee)


l=["mina","nagy","ahmed"]
for i in l : 
    print(i)
    # print("Hello")

l=["mina","nagy","ahmed"]



print(list())

for i in  range(len(l)): 
    print(i," : ",l[i])
    # print("Hello")
print("=="*20)

for index,value in enumerate(l):
    print(index ," : ",value)
count=0
string =input("Enter Data : ")
for index,value in enumerate(string):
    print(index ," : ",value)
    if value.lower() in ['a','e','i','u','o']:
        count+=1 #count++


print(count)

#Set 
# Mutable , No Index , Not Orderd  , Unique
set_data={1,1,2,1,3,5}
print(set_data)
print(type(set_data))
#===============================================
string= input("Enter data and remove duplicates")
print(len(set(list(string))))
set_data={1}
set_data.add(2)
#set_data[0]
l=[1,2,3,5,1,5]
print(sum(l))
print(sum(set(l)))
#=================================================

#Evalte True  vs   True Value

#Falsy Value : 0,None ,[],'',{},False
if -1:
    print("hello")

#========================== Switch ==============
# match
i=0
while(i<5) :
    i+=1

print(i)
