a = 0
b = 1
next_num = a
n = int(input())
for i in range(n+1):
    print(next_num, end=" ")
    a = b
    b = next_num
    next_num = a+b
    