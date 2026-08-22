items=["c","python","java","javascript"]
print(items)

print(items[2])
print(items[-2])

items.append("c++")
print(items)#append in last position

items.pop()
print(items)#pop in last position

items.insert(1,"Go")
print(items)

items.remove("java")
print(items)

items.clear()

print(items)

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)
