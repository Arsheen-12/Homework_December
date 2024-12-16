#18. Guess the Number: Implement a number-guessing game where the user has to guess a number between 1 and 100. 
# Provide feedback ("Too High" or "Too Low") until they guess correctly.
n = int(input("Enter a number: "))
g=0
while n!=g:
    g=int(input("Give number: "))
    if g<=n:
        print("Too Low")
    else:
        print("Too High")

#19. Reverse Digits: Write a program to reverse the digits of a number using a while loop.
n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10  
    rev = rev * 10 + digit 
    n = n // 10  
print("Reversed number:", rev)

#20. Fibonacci Series: Generate the first N Fibonacci numbers using a while loop.
n = int(input("Enter how many Fibonacci numbers you want: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    a, b = b, a + b  
    count += 1


