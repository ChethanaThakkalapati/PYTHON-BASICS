'''Output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values using List Comprehension'''
a = input("Enter numbers separated by spaces: ")
numbers = list(map(int, a.split()))

# Create dictionary of odd numbers and their cubes
odd_cubes = {n: n**3 for n in numbers if n % 2 != 0}

# Display the result
print("Dictionary of odd numbers and their cubes:")
print(odd_cubes)


