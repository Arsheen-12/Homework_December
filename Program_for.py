#15. Factorial: Write a program to calculate the factorial of a given number using a for loop.
n= int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact=fact*i  
print(f"The factorial is:",fact)


#16. Multiplication Table: Print the multiplication table of a number entered by the user.
n= int(input("Enter a number: "))
for i in range(1,11):
    print(f'{n}X{i}={n*i}')

#17. Sum of Squares: Calculate the sum of squares of the first N natural numbers.
n= int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i*i
print("Sum of Squares is:",sum)