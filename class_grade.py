"""
Create a list to store 5 number (float)
Capture users's input 5 times for their grades
Each time we capture the users's input, we append the number to the list
Sort the list ascending, then splice the items starting at index 2
Once we have three highest numbers in the list, we sum them up aned divide by 3
Output a message to the user
"""

# grades = []     # empty list

# grade = input("Enter the 1st grade:")    # ask to user to enter grade
# grades.append(float(grade))             # append the given grade to the list as a float

# grade = input("Enter the 2nd grade:")
# grades.append(float(grade))

# grade = input("Enter the 3rd grade:")
# grades.append(float(grade))

# grade = input("Enter the 4th grade:")
# grades.append(float(grade))

# grade = input("Enter the 5th grade:")
# grades.append(float(grade))


# grades.sort()       # sorts the grades ascending 
# grades = grades[2:]     # new grades from index 2 to the end of the original list (which are going to be the 3 highest grades)
# grades = sum(grades)        # adds up the grades in the list
# result = grades/3       # divides the sum into three
# print("The average of the highest three grades is {0:.2f}%".format(result))     # rounds the result to two decimal and place it where curly brackets are


"""CODE REFACTOR USING LOOP"""

grades = []

for i in range(5):      # this loop simplify the previous way to do it
    grades.append(float(input("Enter a grade: ")))

grades.sort()
grades = sum(grades[2:])/3

print("The average of the highest three grades is {0:.2f}%".format(grades))
