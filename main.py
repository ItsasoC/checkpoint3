# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
str1 = "hola mundo"
numb1 = 123
list1 = [1,2,3,4,5]
bool1 = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
str2 = str1[0:3]
print(str2)

# Exercise 3: Use an index to grab the first element from your list.
list2 = list1[0:3]
print(list2)

# Exercise 4: Create a new number variable that adds 10 to your original number.
numb2 = numb1 + 10
print(numb2)

# Exercise 5: Use an index to get the last element in your list.
list3 = list1[-1]
print(list3)

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'

list4 = names.split(',')
print(list4)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
str3 = str1[0].upper()
str3 = str3 + str1[1:]
print(str3)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"El numero elegido es {numb1}")

# Exercise 9: Print “hello world”.
print("hello world")

