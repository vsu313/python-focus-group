#!/usr/bin/env python3

#1 Make a list named `my_list` containing the following information (you will need to format it properly, but keep it in this order): glasses, canvas, soap, photo album, 5084988, 9.2, 3/11, False
my_list = ["glasses", "canvas", "soap", "photo album", 5084988, 9.2, 3/11, False]
print(my_list)

#2 Make the list nested by adding a tuple containing the numbers 1-5 in it
my_tuple = (1, 2, 3, 4, 5)
my_list.append(my_tuple)
print(my_list)

#3 Use indexing to print 5084988 from the list. Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 4 of my list, the value is {my_list[4]}')

#4 Use indexing to print out the number 3 from within the tuple. Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 8 and sub-index 2 of my list, the value is {my_list[8][2]}.')

#5 Use indexing to access the "b" in "photo album." Use an f-string to print the index in addition to the value in the same print statement.
print(f'At index 3 and sub-index 8 of my list, the value is {my_list[3][8]}.')

#6 Slice the list such that only strings are present in your sliced data.
only_str = my_list[0:4]
print(only_str)

#7 Add the word "ideology" between "photo album" and 5084988.
my_list.insert(4, "ideology")
print(my_list)

#8 Change the word "canvas" to "panel."
my_list[1] = "panel"
print(my_list)

#9 Delete 9.2 from the list.
del(my_list[6])
print(my_list)

#10 Print the maximum value present in the tuple. (Hint: Use indexing to access the tuple)
print(max(my_list[-1]))

#11 Use the range function to print the numbers 1-20 ONLY (i.e. do not print 0 or 21)
num_list = list(range(1,21))
print(num_list)