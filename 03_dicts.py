#
myDict = dict( one = 'uno', two = 'dos', three = "tres")
myDict2 = {'one':'uno', 'tho': 'dos', 'three': 'tres' }
#? Delation
myDict2.pop('aa', None) #if the key deoes not exist, not returning an error

myDict.popitem() #Delate the last inseted item
print(myDict)

myDict.clear() #Delete all items in dictionary
print(myDict)

#?Methods
myNew = {}.fromkeys([1,2,3,4], 'Value!') #initialize a dictionary from an array and give all the elements a value
print(myNew)

print(myNew.get('Not exists :)')) #*Return the value of a specified key

print(myNew.keys()) #Print a tuple of the keys
print(myNew.values()) #Print a tuple of the values

#Dictionary comprehension
a = [1,1,1,1,2,33,44,4,5,5,5,33,2,1,1,5,6,3]
b = {i:1 for i in a}
print(b)

