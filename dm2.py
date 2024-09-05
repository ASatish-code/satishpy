# Step I: Create a List
lst = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]

# Step II: Iterate using a for loop
print("Iteration using a for loop:")
for num in lst:
    print(num)

# Step III: Iterate using a for loop and range
print("\nIteration using for loop and range:")
for i in range(len(lst)):
    print(lst[i])

# Step IV: List Comprehension
print("\nUsing List Comprehension:")
squared_list = [x**2 for x in lst]
print(squared_list)

# Step V: Enumerate
print("\nUsing Enumerate:")
for index, value in enumerate(lst):
    print(f"Index {index} has value {value}")

# Step VI: Iter function and next function
print("\nUsing iter and next:")
lst_iter = iter(lst)  # Create an iterator
print(next(lst_iter))  # Get the next element
print(next(lst_iter))  # Get the next element

# Step VII: Map function (let's say we want to multiply each value by 2)
print("\nUsing Map function (multiply by 2):")
mapped_list = list(map(lambda x: x * 2, lst))
print(mapped_list)

# Step VIII: Using zip (let's zip the list with a list of string representations)
print("\nUsing zip function:")
string_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
zipped_list = list(zip(lst, string_list))
print(zipped_list)

# Step IX: Using NumPy Module (Convert list to NumPy array and perform operations)
import numpy as np

np_array = np.array(lst)
print("\nUsing NumPy module (Array representation):")
print(np_array)

print("\nSum of all elements in NumPy array:", np.sum(np_array))
print("Mean of elements in NumPy array:", np.mean(np_array))
