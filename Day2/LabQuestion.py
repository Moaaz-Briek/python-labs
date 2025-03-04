string ="Python is a great programming language"
# 1. Reverse a String
# Write a Python program to reverse a string.
print(string[::-1])
# ========================================================
# 2. Check if a String is a Palindrome
# Write a Python program to check if a string is a palindrome (reads the same backward as forward).
print(string == string[::-1])
# ========================================================
# 3.Remove Duplicates from a String
# Write a Python program to remove duplicate characters from a string.
print(''.join(set(string)))
# =========================================================
# 4.Find the Longest Word in a String
# Write a Python program to find the longest word in a given string.
#Output=programming
print(max(string.split(), key=len))
# ========================================================
# 5.Find Common Elements Between Two Tuples
# Write a Python program to find common elements between two tuples.
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)
print(tuple(set(tuple1) & set(tuple2)))
# ========================================================
# 6.Find the Maximum and Minimum Value in a Dictionary
# Write a Python program to find the maximum and minimum value in a dictionary.
my_dict = {"a": 10, "b": 20, "c": 5}
Min= 5; Max=20
print(f"max={max(my_dict.values())}, min={min(my_dict.values())}")
# ========================================================
# 7- Merge Two Dictionaries
# Write a Python program to merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print({**dict1, **dict2})
# ========================================================
# 8- Find Common Keys in Two Dictionaries
# Write a Python program to find common keys in two dictionaries.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
#Output: {'b', 'c'}
print(set(dict1.keys()) & set(dict2.keys()))
# ========================================================
# 9- takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu
string = input('Enter your name: ')
match=''
for index in range(1, len(string)):
    current = string[index-1]
    next = string[index]
    if (ord(current.lower()) > ord(next.lower())):
        match+=current
        break
    match+=current

print(match)
