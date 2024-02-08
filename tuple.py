
# In Python, a tuple is a collection data type that is similar to a list. However, there are key differences between tuples and lists. The main distinction is that tuples are immutable, meaning their elements cannot be changed or modified after the tuple is created. In contrast, lists are mutable and can be modified.

# Here's a basic overview of tuples:

# Syntax:

# Tuples are created using parentheses ().
# Elements within a tuple are separated by commas.

metro_cities = ("Delhi","Mumbai","Bangalore","Hyderabad")
print(metro_cities)

# Concatenation of the tuple  ( add two or more tuple)
other_cities = ("Nagpur", "Pune", "Mysore", "Cochi")

metro_cities+=other_cities
print(metro_cities)

# Repetation ( to increase the number of times a variable is being printed)

double_cities = metro_cities*2
print(double_cities)

# indexing ( to find the position of a characted in a group)
# print one index
print(metro_cities[1])
#print a range of index
print(metro_cities[0:4])


