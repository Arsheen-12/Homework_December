### Lists
#7. Sum of Elements: Write a program to calculate the sum of all elements in a list.
List=[1,2,3,4,5]
sum=0
for i in List:
    sum=sum+i
print(sum)

#8. Largest Number: Find the largest number in a list without using built-in functions.
List=[10,20,300,40,50,100]
max = 0
for i in List:
    if i > max:
        max = i
print(max)

#9. Reverse a List: Reverse a given list without using built-in methods.
List=[10,20,30,40,50]
i=0
j=len(List)-1
while i<j:
    List[i],List[j]=List[j],List[i]
    i+=1
    j-=1
print(List)


#10. Remove Duplicates: Write a program to remove duplicates from a list.
List=[1,2,2,3,4,5]
