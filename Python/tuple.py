#unlike lists tuples are immutable, meaning they cannot be changed after they are created.
#  They are defined using parentheses () instead of square brackets [].

numbers = (1, 2, 3, 4, 5)
numbers[0] = 10  # This will raise a TypeError because tuples are immutable
print(numbers)  # Output: (1, 2, 3, 4,

#Can be used to store heterogeneous data types
person = ('Alice', 30, 'Engineer')
print(person)  # Output: ('Alice', 30, 'Engineer')
print(person[0])  # Output: Alice   