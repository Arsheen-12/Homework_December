#11. Key Checker: Write a program to check if a given key exists in a dictionary.
dict = {'a': 1, 'b': 2, 'c': 3}
i=input("Enter Key you want to check:")
if i in dict:
    print("Exists")
else:
    print("Not Exists")


#12. Merge Dictionaries: Combine two dictionaries into one.
dict = {'a': 1, 'b': 2, 'c': 3}
dict1={'x':10,'y':20,'z':30}
dict2=dict.copy()
dict2.update(dict1)
print(dict2)

#13. Frequency Counter: Count the frequency of each character in a given string and store it in a dictionary.

string = input("Enter a string: ")
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character frequency:",frequency)



#14. Student Marks: Create a dictionary where keys are student names, and values are their marks. 
# Write a program to find the student with the highest marks.
# Dictionary of students and their marks
stdmarks = {'Arsheen': 87,'Sarah': 93,'sita': 86,'John': 98,'Somu': 90}
maxstudent = ''
marks = 0
for student, mark in stdmarks.items():
    if mark > marks:
        marks = mark
        maxstudent = student
print("Student with the highest marks:")
print("Name:", maxstudent)
print("Marks:", marks)
