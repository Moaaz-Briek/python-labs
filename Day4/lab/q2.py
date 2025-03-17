'''Dataclass is a powerful decorator (@dataclass) that automatically generates common special methods for classes primarily designed to store data.

These methods include __init__, __repr__, __eq__, and others, which significantly reduce the amount of boilerplate code required when defining such classes.

By using dataclasses, we can streamline the creation of classes intended for data storage, making the code more concise and readable.

The @dataclass decorator automatically generates the __init__ method, eliminating the need to manually write an initializer to assign values to instance attributes.

It also generates a __repr__ method, providing a clear and informative string representation of the object.

The __eq__ method is created to enable comparison of objects based on their attributes.

Dataclasses us to specify default values for attributes, making it optional to provide values for those attributes when creating an instance.

Dataclasses rely on type annotations to define the attributes of the class, promoting better code clarity and enabling static type checkers to validate the code.
'''

#Example Usage:

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int
    salary: int = 1000

Employee = Employee(name='Moaaz', age=27)

print(Employee)  # Output: Employee(name='Moaaz', age=27, salary=1000)

'''
Explanation:
The Employee class is defined with three attributes: name, age, and salary.

The salary attribute has a default value of 1000, so it doesn’t need to be provided when creating an instance.

The @dataclass decorator automatically generates the __init__ method, allowing the instance to be created with Employee(name='Moaaz', age=27).

The __repr__ method provides a clear string representation of the object when printed.

Benefits:
Reduced Boilerplate: Dataclasses eliminate the need to manually write repetitive methods like __init__, __repr__, and __eq__.

Improved Readability: The use of type annotations and concise syntax makes the code easier to understand.

Flexibility: Default values and optional attributes provide flexibility in how instances are created.

In summary, dataclasses are a convenient and efficient way to define classes that are primarily used to store data, making Python code cleaner and more maintainable.
'''
