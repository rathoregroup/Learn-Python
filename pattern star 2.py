#nested loop
'''
* * * * *
* * * *
* * *
* *
*
'''
row = int(input())
for i in range(1, row+1):
    for j in range(row - i + 1):
        print("*", end=" ")
    print()








