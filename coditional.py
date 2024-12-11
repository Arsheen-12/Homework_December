#1. # a number  
#Write a program to check if a number is positive, negative, or zero.
b=10
if b>0:
    print("Positive")
elif b<0:
    print("Negative")
else:
    print("Zero")

#2.# even or odd  
#Write a program to check if a given number is even or odd.
a=4
if a%2==0:
    print("Even")
else:
    print("Odd")

#3.Grade Checker  
'''Write a program to display grades based on a percentage:
   - A: 90-100
   - B: 70-89
   - C: 50-69
   - F: Below 50'''
per=40
if 90<=per<=100:
    print("A")
elif 70<=per<=89:
    print("B")
elif 50<=per<=69:
    print("C")
else:
    print("F")

#4.# divisibility  
## if a given number is divisible by 3, 5, or both.

m=15
if m%3==0 and m%5==0:
    print("Divisible by both")
elif m%5==0:
    print("Divisible by 5")
else:
    print("Divisible by 3")

#5.Minimum of two numbers
#Find the smaller number between two given numbers.

a=10
b=20
if(a<b):
    print("a is Minimum")
else:
    print("b is Minimum")

#6.Find the largest of three numbers
#Given three numbers, find the largest using nested if statements.

a=10
b=20
c=40
if a>b:
    print("a is largest")
else:
    if b>c:
        print("b is largest")
    else:
        print("c is largest")
    
#7.# leap year
#Write a program to check if a given year is a leap year or not:
num=2000
if num%4==0 and num%100!=0 or num%400==0:
    print("Leap Year!!!!")

#8.Categorize temperature into:
#Cold: Below 15°C
#Warm: 15°C to 30°C
#Hot: Above 30°C

temp=19
if temp<15:
    print("Cold")
elif temp>=15 and temp<=30:
    print("Warm")
else:
    print("Hot")

#9.Vowel or consonant
## if a given character is a vowel or consonant.
char='E'
if char=='a' or char=='A':
    print("Vowel")
elif char=='e' or char=='E':
    print("Vowel")
elif char=='i' or char=='I':
    print("Vowel")
elif char=='o' or char=='O':
    print("Vowel")
elif char=='u' or char=='O':
    print("Vowel")
else:
    print("Consonant")

#10.
## if a person is eligible to drive:
#Must be 18 or older.
#Nested check for possessing a valid license.

age=19
if age>=18:
    print("Eligible to drive")
else:
    print("Not Eligible to drive")

#11.Triangle validation
## if three sides can form a triangle

a=10
b=30
c=30
if a+b>c and b+c>a and c+a>b:
    print("It can form Triangle")
else:
    print("It cannot form Triangle")

#12.Calculate tax based on salary
#Determine the tax rate:
#Salary ≤ 5,00,000: 5%
#5,00,001 - 10,00,000: 10%
#Above 10,00,000: 20%

salary=700000
if salary<=500000:
    print("tax=5%")
elif salary<=500001 or salary<=1000000:
    print("tax=10%")
else:
    print("tax=20%")

#13.Categorize age
#Categorize a person's age:
#0-12: Child
#13-19: Teen
#20-59: Adult
#60+: Senior

age=15
if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teen")
elif 20<=age<=59:
    print("Adult")
else:
    print("Senior")

#14.Logical AND check
## if a number is greater than 10 and divisible by 2.
num=5
if num>10 and num%2==0:
    print("True")
else:
    print("False")

#15.Logical OR check
## if a number is less than 5 or greater than 20.
num=25
if num<5 or num>20:
    print("True")
else:
    print("False")

#16.Electricity bill
#Calculate an electricity bill:
#Usage ≤ 100 units: ₹5/unit
#101-200 units: ₹10/unit
#Above 200 units: ₹15/unit

unit=10
if unit<=100:
    print("₹5/unit")
elif 101<=unit<=200:
    print("₹10/unit")
else:
    print("₹15/unit")

#17.Season finder
#Find the season based on the month:
#December-February: Winter
#March-May: Spring
#June-August: Summer
#September-November: Autumn

Season="November"
if Season=="December" or Season=="January" or Season=="February":
    print("Winter")
elif Season=="March" or Season=="April" or Season=="May":
    print("Spring") 
elif Season=="June" or Season=="July" or Season=="August":
    print("Summer")
elif Season=="September" or Season=="October" or Season=="November":
    print("Autumn")
else:
    print("Invalid")

#18.Password validation
#Check if a password meets these conditions:
#At least 8 characters.
#Contains the character '@'.

Password='Arsheen@11'
if '@' in Password and Password>='8':
    print("Valid Password")
else:
    print("Invalid Password")

#19.Categorize BMI
#Categorize Body Mass Index (BMI):
#Below 18.5: Underweight
#18.5 - 24.9: Normal
#25 - 29.9: Overweight
#30 or higher: Obese

BMI=40
if BMI<18.5:
    print("Underweight")
elif 18.5<=BMI<=24.9:
    print("Normal")
elif 25<=BMI<=29.9:
    print("Overweight")
elif BMI>=30:
    print("Obese")
else:
    print("Invalid")

#20.Character type checker
#Check if a given character is:
#Alphabet
#Digit
#Special character

char='@'
if 'a'<=char<='z' or 'A'<=char<='Z':
    print("Alphabet!!!")
elif '0'<=char<='9':
    print("Digit!!!")
else:
    print("Special Character!!!")





