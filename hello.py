# 1. Variables and Data Types
# Variables store data and are created by simply assigning a value to a name.
# Python is dynamically typed, so you don't need to declare the type explicitly.



# 4. Functions
# Functions are defined using the 'def' keyword.



def greet(name):
    return f"Hello, {name}!"


# python

# //adds numbers togeher
def add_numbers(a, b):
    """
    Adds two numbers (int or float) and returns the result.
    """
    
    return "My age is", a+b

# Example usage:
age = add_numbers(28, 5)
name = greet("Blain")

print(name, age)





def check_number(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    return "Zero"

print(check_number(10))  # Output: "Positive"
print(check_number(-5))  # Output: "Negative"
print(check_number(0))   # Output: "Zero"



def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Returns a tuple with both values

q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")



def is_even(number):
    """
    Returns True if the number is even, False if odd.
    """
    return number % 2 == 0

# Example usage:
print(is_even(4))  # Output: True
print(is_even(7))  # Output: False





def concatenate_strings(str1, str2):
    """
    Concatenates two strings and returns the result.
    """
    return str1 + str2

# Example usage:
full_name = concatenate_strings("John ", "Doe")
print(full_name)  


# python

# def find_max(numbers):
#     """
#     Returns the maximum number in a list of integers or floats.
#     """
#     if not numbers:
#         return None  # Return None if the list is empty
#     return max(numbers)

# # Example usage:
# max_number = find_max([3, 7, 2, 9, 4])
# print(max_number)  # Output: 9

# 4. Function to Count the Occurrences of a Word in a String:

# python

# def count_occurrences(text, word):
#     """
#     Counts how many times a word occurs in a given string.
#     """
#     words = text.split()  # Split the text into a list of words
#     return words.count(word)

# # Example usage:
# text = "hello world hello universe hello"
# word_count = count_occurrences(text, "hello")
# print(word_count)  # Output: 3

# 5. Function to Print Information from a Dictionary:

# python

# def print_person_info(person):
#     """
#     Prints the information of a person given a dictionary with keys 'name', 'age', and 'city'.
#     """
#     print(f"Name: {person['name']}")
#     print(f"Age: {person['age']}")
#     print(f"City: {person['city']}")

# # Example usage:
# person_info = {"name": "Alice", "age": 28, "city": "New York"}
# print_person_info(person_info)
# # Output:
# # Name: Alice
# # Age: 28
# # City: New York

# 6. Function to Calculate the Square of Each Number in a List:

# python

# def square_numbers(numbers):
#     """
#     Returns a list of squares of each number in the input list.
#     """
#     return [x ** 2 for x in numbers]

# # Example usage:
# squared_list = square_numbers([1, 2, 3, 4])
# print(squared_list)  # Output: [1, 4, 9, 16]

# 7. Function to Check If a Number is Even or Odd:

# python

# def is_even(number):
#     """
#     Returns True if the number is even, False if odd.
#     """
#     return number % 2 == 0

# # Example usage:
# print(is_even(4))  # Output: True
# print(is_even(7))  # Output: False

# 8. Function to Reverse a String:

# python

# def reverse_string(s):
#     """
#     Returns the reverse of the input string.
#     """
#     return s[::-1]

# # Example usage:
# reversed_str = reverse_string("hello")
# print(reversed_str)  # Output: "olleh"







# # 3. Loops: For and While
# # For loop iterates over a sequence (like a list or range).
# for i in range(5):  # range(5) generates numbers 0 to 4
#     print(i)

# # While loop continues until the condition is False.
# count = 0
# while count < 5:
#     print(count)
#     count += 1  # Increment count by 1



# # 5. Lists
# # Lists are ordered, mutable collections of items.
# fruits = ["apple", "banana", "cherry"]
# fruits.append("date")  # Add an item to the list
# print(fruits[0])  # Access the first item in the list

# # 6. Dictionaries
# # Dictionaries are key-value pairs.
# person = {
#     "name": "Bob",
#     "age": 30,
#     "city": "New York"
# }

# print(person["name"])  # Access value by key

# # 7. Error Handling
# # Use try-except blocks to handle exceptions (errors) gracefully.
# try:
#     result = 10 / 0  # This will cause a ZeroDivisionError
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # 8. Classes and Objects
# # Python supports Object-Oriented Programming (OOP).
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name  # Instance variable
#         self.breed = breed

#     def bark(self):
#         return f"{self.name} says woof!"

# # Creating an object (instance of a class)
# my_dog = Dog("Rex", "Labrador")
# print(my_dog.bark())

# # 9. List Comprehensions
# # A concise way to create lists.
# squares = [x ** 2 for x in range(10)]  # Generates a list of squares of numbers 0-9
# print(squares)

# # 10. Importing Modules
# # Use 'import' to bring in external libraries/modules.
# import math
# print(math.sqrt(16))  # Using the sqrt function from the math module
