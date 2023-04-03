n = int(input(""))
temp = n
for i in range(1, n+1) 
    if 
        c = 0
        while(n>0):
            n = n//10
            c = 1+c

        n = temp
        sum = 0
        for i in range(c):
            r = n%10
            sum = sum + r**c
            n = n//10
        if sum==temp:
            print("Yes")
        else:
            print("No")
