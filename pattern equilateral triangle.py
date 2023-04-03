#nested loop
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
row = int(input())
for i in range(1, row+1):
    for j in range(row, 0 ,-1):
        if j>i:
            print("", end = " ")
        else:
            print("*", end=" ")
    print()









