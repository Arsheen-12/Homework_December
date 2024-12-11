#1. Print Each Character in a String
word = "Python"
for char in word:
    print(char)

#2. Print Numbers in a Range
for num in range(1, 6):#1,2,3,4,5
    print(num)

#3. Sum of Numbers in a List
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Sum:", total)

#4. Print Even Numbers in a Range
for num in range(2, 11, 2):
    print(num)

#5. Iterate Through a List of Fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

#6. Use for Loop with break
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at", num)
        break
    print(num)

#7. Use for Loop with continue
for num in range(1, 6):
    if num == 3:
        continue  # Skip the rest of the loop for this iteration
    print(num)

#8. Nested for Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

#9. Iterate Over a Dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

#10. Print Multiplication Table
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

