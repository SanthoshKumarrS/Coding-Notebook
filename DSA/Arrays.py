#Arrays

# arrays_example.py

# ----------------------------------
# Creating an array (Python list)
# ----------------------------------

numbers = [10, 20, 30, 40, 50]

print("Original Array:", numbers)

# ----------------------------------
# Accessing elements
# ----------------------------------

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# ----------------------------------
# Updating an element
# ----------------------------------

numbers[2] = 35

print("After Update:", numbers)

# ----------------------------------
# Adding elements
# ----------------------------------

numbers.append(60)          # Add at end
numbers.insert(1, 15)       # Insert at index 1

print("After Adding:", numbers)

# ----------------------------------
# Removing elements
# ----------------------------------

numbers.remove(40)          # Remove by value
removed = numbers.pop()     # Remove last element

print("Removed:", removed)
print("After Removing:", numbers)

# ----------------------------------
# Traversing the array
# ----------------------------------

print("\nTraversing:")

for num in numbers:
    print(num)

# ----------------------------------
# Traversing with index
# ----------------------------------

print("\nIndex Traversal:")

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

# ----------------------------------
# Searching
# ----------------------------------

target = 35

if target in numbers:
    print(f"\n{target} found at index {numbers.index(target)}")
else:
    print(f"\n{target} not found")

# ----------------------------------
# Length
# ----------------------------------

print("\nLength:", len(numbers))

# ----------------------------------
# Maximum & Minimum
# ----------------------------------

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# ----------------------------------
# Sum & Average
# ----------------------------------

print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

# ----------------------------------
# Sorting
# ----------------------------------

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("\nAscending:", ascending)
print("Descending:", descending)

# ----------------------------------
# Reverse
# ----------------------------------

numbers.reverse()

print("Reversed:", numbers)

# ----------------------------------
# Slicing
# ----------------------------------

print("\nFirst 3:", numbers[:3])
print("Last 2:", numbers[-2:])
print("Middle:", numbers[1:4])

# ----------------------------------
# Copy
# ----------------------------------

copy_array = numbers.copy()

print("\nCopied Array:", copy_array)

# ----------------------------------
# 2D Array
# ----------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n2D Array:")

for row in matrix:
    print(row)

print("\nCenter Element:", matrix[1][1])