def minimum(first, second):
    if first>second:
        return second
    else:
        return first


num1 = int(input())
num2 = int(input())
result = minimum(num1, num2)
print(result)