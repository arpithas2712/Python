# my_tuple= (element1,element2,element3.....) 

fruit=("apple","banana","cherry")
number=(1,2,3,4)

print(fruit[0])

fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

print(fruits[1:3])  # Output: ('banana', 'cherry')

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

repeated_tuple = (1, 2) * 3
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

print("apple" in fruits)  # Output: True

my_tuple = (1, 2, 3, 1, 1)
print(my_tuple.count(1))  # Output: 3

my_tuple = ("apple", "banana", "cherry")
print(my_tuple.index("banana"))  # Output: 1

#Sets in Python

fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}

empty_set = set()

#Set Operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
print(union_set)

intersection_set = set1 & set2  # Output: {3}
print(intersection_set)

difference_set = set1 - set2  # Output: {1, 2}y
print(difference_set)

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
print(sym_diff_set)

#Set Methods

fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry'}

fruits_set.discard("banana")  # No error if "banana" is not in the set
print(fruits_set)

fruits_set.pop()
print(fruits_set)


fruits_set.clear()
print(fruits_set)