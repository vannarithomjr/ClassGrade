"""
Create a list to store 5 number (float)
Capture users's input 5 times for their grades
Each time we capture the users's input, we append the number to the list
Sort the list ascending, then splice the items starting at index 2
Once we have three highest numbers in the list, we sum them up aned divide by 3
Output a message to the user
"""

grades = []

grade = input("Enter the 1st grade:")
grades.append(float(grade))

grade = input("Enter the 2nd grade:")
grades.append(float(grade))

grade = input("Enter the 3rd grade:")
grades.append(float(grade))

grade = input("Enter the 4th grade:")
grades.append(float(grade))

grade = input("Enter the 5th grade:")
grades.append(float(grade))


grades.sort()
grades = grades[2:]
grades = sum(grades)
result = grades/3
print("The average of the highest three grades is {0:.2f}%".format(result) )