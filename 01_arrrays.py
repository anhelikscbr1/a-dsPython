#* Python lists (arrays)

#? Append and insert
a = []
a.append(3)
a.append(93)
a.append(-2)
a.insert(0,-1);
print(a)

#? Is there an element in the array?
print(5 in a) #False
print(1 in a) #True

#? Slice
print(a[:len(a)])
print(a[1:3])

#?Update an array by slicing
myFirstArr = [0,0, 'March', 'Aprli', 'June']
print('MyFirstArr: ' + str(myFirstArr))
myFirstArr[:2] = ['January', 'February'] 
print('MyFirstArr: ' + str(myFirstArr))
print()

#? Delation 
myArr = [0,1,2,3,4]
print("myArr: " + str(myArr))
myArr.pop() #Delates the last element O(1)
myArr.pop(0) #Delates the first element O(n)
print("myArr: " + str(myArr))

myArr.remove(1) #Remove by value
print("myArr: " + str(myArr))

del myArr[0] #remove by index
print("myArr: " + str(myArr))

del myArr[:] #Delate all the elements of the array
print("myArr: " + str(myArr))

c = [4,65,8,9,4,2,1,3,5,65,5,5,3]
d = sorted(c)
print(c)
print(d)

#? List comprehension
myprevList = [0,1,2,3,4,5]
newList = [i*i for i in myprevList]
print('New List: ' + str(newList))

#? List comprehension conditionals
newEvenNumbers = [i for i in myprevList if i % 2 == 0]
newOddNumbers = [i for i in myprevList if i % 2 != 0]
print('Even numbers: ' + str(newEvenNumbers))
print('Odd numbers: ' + str(newOddNumbers))

#?Lis compreghension example: return all the vowels


myPhrase = "En un lugar de la mancha de cuyo nombre no quiero acordarme"
myVowels = [letter for letter in myPhrase if letter in "aeiou"] 
print(myVowels) 