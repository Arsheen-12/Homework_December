n = int(input())
flag = False
for i in range(2, n, 1):
    if n % i == 0:
        flag = True
        break
if flag:
    print("Not Prime")
else:
    print("Prime")


n = int(input())
i = 2
while i <= n:
    j = 2
    flag = False
    while j < i:
        if i % j == 0:
            flag = True
            break
        j = j + 1
    if (not(flag)):
        print(k)
    i =  i + 1