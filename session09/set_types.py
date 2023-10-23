#!/usr/bin/env python3

# Creating a set using list to set type-casting
album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)


# Try adding an element to the set
album_set.add("Back in Black")
print(album_set)


# Remove element from set
album_set.remove(10.0)
print(album_set)


# Verify element presence in a list
exists = "Back in Black" in album_set
print(exists)

no_exists = "Pillow" in album_set
print(no_exists)


# Find intersecting elements in lists
another_album_set = {"Thriller", "Closer", "The Queen is Dead", "Born in the USA", "Synchronicity"}
my_intersections1 = album_set & another_album_set
print(my_intersections1)

my_intersections2 = album_set.intersection(another_album_set)
print(my_intersections2)


# Find elements unique to each set
unique_to_album_set = album_set.difference(another_album_set)
unique_to_another_album_set = another_album_set.difference(album_set)
print(f'My album_set is {album_set} and another_album_set is {another_album_set}. {unique_to_album_set} are unique to album_set and {unique_to_another_album_set} are unique to another_album_set') 


# Combine sets
combined_sets = album_set.union(another_album_set)
print(combined_sets)


# Demonstrate lack of duplicates in sets
duplicated_list = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
print(duplicated_list)

duplicated_list_as_set = set(duplicated_list)
print(duplicated_list_as_set)


# Supersets and subsets 
my_subset = {'A', 'B', 'C'}
my_superset = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}

# Check if a set is a superset
check_superset1 = my_superset.issuperset(my_subset)
print(check_superset1)
check_superset2 = my_subset.issuperset(my_superset)
print(check_superset2)

# Check if a set is a subset
check_subset1 = my_superset.issubset(my_subset)
print(check_subset1)
check_subset2 = my_subset.issubset(my_superset)
print(check_subset2)