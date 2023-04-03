#empty dictionary not empty set.
set1 = {}
print(type(set1))

#empty set can be created as:

a = set()
print(type(a))
#methods
a.add(4)
a.add(8)
a.add((46,48,8,48))
#a.add([4153,185,6])	#tuple cannot be added in a set.
print(a)

set = {1, 2, 3, 4, 6, 5, 7, 8}
print(type(set))

print(set)
print("\n")

set.add(99)
print(set)

print(len(set))

set.remove(99)
print(set)

print(set.pop())


a = {1,5,5}
print(a)
a.add(45)
print(a)
#operation in set
b01 = a.union({455})
print(b01)
b = a.intersection({5})
print(b)
c = a.difference({5})
print(c)
x = a.pop()
print(x)