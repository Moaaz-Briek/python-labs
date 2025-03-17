'''
Python's multiple inheritance allows a class to inherit attributes and methods from multiple parent classes.

The order in which these parent classes are searched for methods and attributes is determined by the Method Resolution Order (MRO), which is computed using the C3 linearization algorithm.

This algorithm ensures a logical, consistent, and predictable inheritance sequence.

MRO dictates the sequence in which base classes are traversed when accessing a method or attribute.

The C3 algorithm follows three core principles:

Inheritance Hierarchy: The order respects the structure of the inheritance graph.

Local Priority: A class is checked before its superclasses.

Consistency: The order remains stable and predictable across the inheritance hierarchy.

The MRO of a class can be inspected using the __mro__ attribute or the mro() method.
'''
# Example

class Animal:
    def method(self):
        print('Hello from Animal')

class Dog(Animal):
    def method(self):
        print('Hello from Dog')

class Cat(Animal):
    def method(self):
        print('Hello from Cat')

class Monkey(Dog, Cat):
    pass

monk = Monkey()
print(Monkey.__mro__)
#(<class '__main__.Monkey'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)

'''
In this example:

The MRO for class Monkey is Monkey -> Dog -> Cat -> Animal -> object.

When d.method() is called, Python follows the MRO to locate the method, finding it first in class B.

Using __mro__ or mro() help inspecting the inheritance order of a class.
'''
