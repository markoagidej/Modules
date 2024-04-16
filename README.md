1. Python Modules and Data Handling Assignment
Objective:
The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

Task 1: Your Mood Today

Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered.
Code Example:
```python
# mood_responses.py
def mood_response(mood):
# Implement your response logic here
# main.py
import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

```
Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.
2. Exploring Python Modules and Data Structures Assignment
Objective:
The aim of this assignment is to deepen your understanding of Python modules, both built-in and custom, and to enhance your skills in working with various Python data structures like lists, dictionaries, and sets. This assignment focuses on practical applications of these concepts in real-world scenarios.

Task 1: Contact List Manager

Problem Statement: Create a Python script using a custom module to manage a contact list. The script should allow adding, removing, and displaying contacts stored in a list.
Code Example:
    # contacts_manager.py
    # Define functions to add, remove, and display contacts

    # main.py
    # Implement the logic to interact with the contact manager
Expected Outcome: The program should accurately display the current month and year and successfully convert a user-input date string (e.g., "2023-03-15") into a datetime object, handling any invalid inputs gracefully.
3. Mastering Python Modules and Aliases
Objective:
The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases. This will develop your skills in organizing code, simplifying access to module components, and effectively managing namespace in Python programs.

Task 1: Custom Module with Aliases

Problem Statement: Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
Code Example:
```python
# text_utils.py
def reverse_string(s):
# function to reverse a string
def capitalize_string(s):
    # function to capitalize a string

# main.py
# Import text_utils using an alias and utilize its functions

```
Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.