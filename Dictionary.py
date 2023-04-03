dict = {
    "Key" : "Value",
    "Print" : "Hello",
    "list" : [56,486,4,6],
    "Friend" : "Python"
    }

print(dict.items())		#for items in dictionary.
print(list(dict.items()))
print("\n")

print(dict.keys())		#for keys. 
print(list(dict.keys()))
print("\n")

print(dict)		#to update a dictionary.
dict.update({"Friend":"C programming"})
print(dict)
print("\n")

print(dict.get("list"))		#to get the value of specified keys.
print(dict.values())
print(tuple(dict.values()))
dict.clear()
print(dict)
