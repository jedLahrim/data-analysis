# todo 1. for Loop
# Example list
numbers = [1, 2, 3, 4, 5]

# For loop to iterate over the list
for number in numbers:
    print(number)
print('----------------------------------------------')
# todo 2. while Loop
# Initialize a variable
count = 1

# While loop to print numbers from 1 to 5
while count <= 5:
    print(count)
    count += 1
print('----------------------------------------------')
# todo 3. Nested Loops
# Example lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Nested for loop to iterate over both lists
for number in list1:
    for letter in list2:
        print(f'{number} with {letter}')
print('----------------------------------------------')
# todo 3 triple Nested Loops
# Example lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['triple']

# Nested for loop to iterate over both lists
for number in list1:
    for letter in list2:
        for triple in list3:
            print(f'{number} with {letter} and {triple}')
print('----------------------------------------------')
# todo 4. Loop Control Statements
# Example list
numbers = [1, 2, 3, 4, 5]

# For loop with a break statement
for number in numbers:
    if number == 3:
        break
    print(number)

# For loop with a continue statement
for number in numbers:
    if number == 3:
        continue
    print(number)

# For loop with a pass statement
for number in numbers:
    if number == 3:
        pass
    print(number)
print('----------------------------------------------')
# todo 5. else in Loops

# Example list
numbers = [1, 2, 3]

# For loop with an else statement
for number in numbers:
    print(number)
else:
    print("Loop completed without break")

# Initialize a variable
count = 1

# While loop with an else statement
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed without break")
print('----------------------------------------------')

# Sample list
fruits = ["apple", "banana", "cherry"]

# Using a for loop with range to get indexes
for index in range(len(fruits)):
    print(f"Index: {index}, Fruit: {fruits[index]}")

print('List Comprehension----------------------------------------------')
# Using list comprehension to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

# with loop
# Using a for loop to create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = []

for x in numbers:
    squares.append(x ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]
print('----------------------------------------------')
# Using list comprehension to find even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x * 2 for x in numbers if x % 2 == 0]

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# with loop
# Using a for loop to find even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)  # Output: [2, 4, 6, 8, 10]

print('Lambda----------------------------------------------')
(lambda x: x ** 2)(2)

print((lambda x, y: x + y(x))(2, lambda x: x + 23))
