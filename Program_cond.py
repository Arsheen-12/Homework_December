### Condition Flow
#4. Even or Odd: Write a program that checks if a number entered by the user is even or odd.
n=eval(input("Enter n:"))
if n%2==0:
    print("Even")
else:
    print("Odd")


#5. Vowel or Consonant: Accept a character from the user and determine whether it is a vowel or a consonant.
char=input("Enter Character:")
if char=='a' or char=='A' or char=='e' or char=='E' or char=='i' or char=='I' or char=='o' or char=='O' or char=='u' or char=='U':
    print("Vowel")
else:
    print("Consonant")



#6. Grade Calculator: Input a percentage and output a grade according to the following:
  # - 90-100: A
   #- 80-89: B
  # - 70-79: C
   #- 60-69: D
   #- Below 60: F

per=int(input("Enter Percentage:"))
if 90<=per<=100:
    print("A")
elif 80<=per<=89:
    print("B")
elif 70<=per<=79:
    print("C")
elif 60<=per<=69:
    print("D")
else:
    print("F")