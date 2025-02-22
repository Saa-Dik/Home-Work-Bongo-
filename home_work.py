#Part--1:

"""Exercise 01: Write a program to find the length of the variable name
Variable, name="Hello there"""

name="Hello there"
print(len(name))


"""
Exercise 02: Write a program to find the type of the variable name
name=”Hello there”"""

name="Hello there"
print(type(name))


"""Exercise 03: Write a function that takes 2 numbers as arguments (age of two brothers)
and find who is elder
Hints: Use condition inside the function"""

number_1 = float(input("Enter first brother age: "))
number_2 = float(input("Enter second brother age: "))
def number(number_1, number_2):
    if(number_1 > number_2):
        return("The first brother is elder")
    elif(number_2 > number_1):
        return("The second brother is elder")
    else:
        return ("Both are same age")
print(number(number_1, number_2))


"""Exercise 04: Write a program to find the index of 7"""

numbers=[3, 5, 1, 9, 7, 2, 8 ]
index = numbers.index(7)
print(index)


"""Exercise 05: Write a program to sort the numbers in Ascending order"""
numbers=[3, 5, 1, 9, 7, 2, 8 ]
numbers.sort()
print(numbers)


"""Exercise 06: Write a function named “isLandscape” that takes 2 numbers (image width
and height) as arguments and the function returns Landscape if the image width has a
higher value than height. Returns Portrait otherwise
Hints: Use condition inside the function"""
def isLandscape(width,height):
    if (width > height):
        return("Landscape")
    else:
        return("Portrait")
print(isLandscape(1920, 1080))
print(isLandscape(1080, 720))


"""
Exercise 07: FizzBuzz Exercise
Write a function that takes 1 number as argument. The function should return “Fizz” if
the number is divisible by 3, the function should return “Buzz” if the number is divisible
by 5, the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
otherwise return “Not a Fizz-buzz number”
Hints: Use condition inside the function
"""

def FizzBuzz(nums):
  if nums % 3 == 0:
    return ("Fizz")
  elif nums %5 == 0:
    return("Buzz")
  elif nums % 3 == 0 and nums % 5 == 0:
    return ("FizzBuzz")
  else:
    return("Not a Fizz-buzz number")
print(FizzBuzz(10))
print(FizzBuzz(5))
print(FizzBuzz(0))
print(FizzBuzz(8))


"""Exercise 08: Guessing game
Write a function that takes a number 1 to 9 from the user input (use input function inside
a function). Store a number in a variable (let’s assume 6). If the input value is less than
the variable, print (your guess is almost there), if the input value is greater than the
variable, print - your guess is higher, if the input value and variable are equals, print -
Your Guess Is Correct!"""

def Guessing_num():
  user_input = int(input("Enter the Guess Number : "))
  number =  int(input("Enter the Target Number : "))
  if user_input < number:

    print ("your guess is almost there")
  elif user_input > number:
    print ("your guess is higher")
  else:
    print ("Your Guess Is Correct!")
Guessing_num()


"""Exercise 09: Find if 6 available in the list [‘4, 8, 7, 4,3,6,2,1,9’]"""

list = [4, 8, 7, 4,3,6,2,1,9]
if 6 in list:
  print ("In available ")
else:
  print("Unavailable")

"""Exercise 05: Sort the list in DESCENDING order and find the subtraction of
maximum and minimum numbers.list_1 = [4, 9, 8, 7, 5, 2, 13]"""

list_1 = [4, 9, 8, 7, 5, 2, 13]
list_1.sort(reverse=True)

max = list_1[0]
min = list_1[-1]

subtraction_of = max - min

print(list_1)
print(f"Maximum number: {max}")
print(f"Minimum number: {min}")
print(f"Subtraction of maximum and minimum: {subtraction_of}")


"""Find the common items between the lists and make SUM of
the new list items which are common between the lists.
list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]"""

list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]
common_items = list(set(list1) & set(list2))

sum_common_items = sum(common_items)

print(f"Common items: {common_items}")
print(f"Sum of common items: {sum_common_items}")


"""Exercise 06: Write conditional statements to identify the student’s average
marks. If any subject’s mark is less than 40, you should print FAILED
instead of making average marks
student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46"""

def calculate_average(marks):
    # Check if any mark is less than 40
    if any(mark < 40 for mark in marks):
        return "FAILED"
    else:
        # Calculate the average marks
        average_marks = sum(marks) / len(marks)
        return average_marks

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

# Calculate and print results for each student
result_1 = calculate_average(student_1)
result_2 = calculate_average(student_2)

print(f"Student 1: {result_1}")



dict_1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict_2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

keys = set(dict_1.keys()) & set(dict_2.keys())
items = {key: dict_1[key] for key in keys}

print(items)


# Part2 :--

"""Exercise 01 : find the list below is the collection of the ages of people from a
village. Clean up the data and store only numbers in another list.
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
"""
data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
age = []
for x in data_list:
  if isinstance (x, int):
    age.append(x)
print(age)

"""Exercise 03: Find the common items between the lists and make SUM of
the new list items which are common between the lists.
list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]"""

import numpy as np
list_1 = [3, 5, 7, 4, 8, 8]
list_2 = [4, 9, 8, 7, 1, 1, 13]

common_number = np.intersect1d(list_1,list_2)
print(common_number)

"""Exercise 04: Compare the two dictionaries and find the common items
based on KEYs of the dictionaries
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}"""

dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}
common_dict = set(dict1).intersection(dict2)
for key in sorted(common_dict):
    print(key, dict1[key])

"""Exercise 05: Sort the list in DESCENDING order and find the subtraction of
maximum and minimum numbers.
list_1 = [4, 9, 8, 7, 5, 2, 13]"""

list_1 = [4, 9, 8, 7, 5, 2, 13]
list_1.sort(reverse=True)
print(list_1)

"""Exercise 06: Write conditional statements to identify the student’s average
marks. If any subject’s mark is less than 40, you should print FAILED
instead of making average marks
student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]"""

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

if len(student_1) >= 40 and len(student_2) >= 40:
  print("Passed")
else:
     print("falled")
