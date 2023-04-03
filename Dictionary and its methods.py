myDict = {
    "Fast" : "In a quick manner",
    "Harshit" : "A Coder",
    "Marks" : [1,2,3],
    "anotherdict" : {"Mario" : "Player"}, 
    1 : 2
    }

#print(myDict["Fast"])
#print(myDict["anotherdict"]["Mario"])
#myDict["Marks"] = [165,56]
#print(myDict["Marks"])

# Dictionary Methods
print(list(myDict.keys()))	#Print the keys of the dict.
print(list(myDict.values()))	#Print the values of the dict.
print(list(myDict.items()))

updateDict = {
    "Hello" : "Namaste"
    }
myDict.update(updateDict)
print(myDict)















