# Task 1: Custom Module with Aliases

import text_utils as txt_util

my_string = input("Input a string!\n")

print("What would you liek to do with this string?")
print("1. Reverse the string")
print("2. Capitalize the string")

choice = input()

if choice == "1":
    new_string = txt_util.reverse_string(my_string)
elif choice == "2":
    new_string = txt_util.capitalize_string(my_string)
else:
    print("Choose 1 or 2!")
    exit()

print(f"Here is your new string:\n{new_string}")