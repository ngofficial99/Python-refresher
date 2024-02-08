# In Python, a list is a versatile and mutable data type that allows you to store and manipulate a collection of items. Here are some key characteristics and operations associated with lists:

# Syntax:

# Lists are created using square brackets [].
# Elements within a list are separated by commas.

productInfo1 = ["Samsung", "Galaxy s24", 10000.99, 2024]
print(productInfo1)

# concatenation (adding two  or more lists together)

productInfo2 = ["Google", "Pixel 8 pro", 90000.70, 2023]
products = productInfo1+productInfo2
print(products)
productInfo1+=productInfo2
print(productInfo1)


#remove an element from the list 

productInfo1.remove("Samsung")
print(productInfo1)


# repetition in lists 

print(productInfo2*3)

# Slicing ( to have a specific portion of a list use the starting index number and the last index number + 1)

print(productInfo2[0:2])

# appending ( adding a value to the list)
productInfo2.append("On sale")
print(productInfo2)

#extend ( used to add multiple elements to a list)

classmate = ["nishant", "Anamika", "Keshav", "Abhishek"]
classmate.extend(["Pratirath", "Shamun"])

print(classmate)

classmate.append(productInfo1)
print(classmate)

# insert ( to insert any element at a particular position )

classmate.insert(2,"Roshan")
print(classmate)


