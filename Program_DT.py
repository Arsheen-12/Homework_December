#Python Data Types
#1. Check the Type: Write a program to take an input from the user and print its data type.
n=eval(input("Enter n:"))
print("Data type is:",type(n))

#2. Simple Arithmetic: Accept two numbers from the user and perform addition, subtraction, multiplication, 
# and division.
a=eval(input("Enter a:"))
b=eval(input("Enter b:"))
print("Addition is:",a+b)
print("Subtraction is:",a-b)
print("Multiplication is:",a*b)
print("Division is:",a/b)

#3. Temperature Converter: Convert a given temperature from Celsius to Fahrenheit and vice versa.

f=int(input("Enter f:"))
c=int(input("Enter c:"))
f=(9/5 * c) + 32
print("Celcius to Fahrenheit:",f)
c = (f - 32) * 5/9
print("Fahrenheit to Celcius:",c)




