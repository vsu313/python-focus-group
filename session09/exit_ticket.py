#!/usr/bin/env python3

#1 Make a dictionary called my_dict where the keys are confusion, recording, organization, complaints, soup and the values are True, No, 57, [1, 2, 3], alphabet, respectively.
my_dict = {'confusion':True, 'recording':'No', 'organizaton':57, 'compaints':[1, 2, 3], 'soup':'alphabet'}

#2 Print the key corresponding the recording.
print(my_dict['recording'])

#3 Add the key and value set catastrophe and False, respectively.
my_dict['catastrophe'] = False
print(my_dict)

#4 Delete the recording entry and its corresponding value.
del(my_dict['recording'])
print(my_dict)

#5 Check if "soup" is in the dictionary.
check1 = 'soup' in my_dict
print(check1)


#6 Print all the keys in the dictionary.
print(my_dict.keys())

#7 Print all the values in the dictionary.
print(my_dict.values())

#8 Make a list containing the following: Balalaika, Bouqet, Outlook, Petticoat, Summit, Chime, Labourer, Patty, Persimmon, Sample.
list = ['Balalaika', 'Bouqet', 'Outlook', 'Petticoat', 'Summit', 'Chime', 'Labourer', 'Patty', 'Persimmon', 'Sample']
print(list)

#9 Turn the list into a set called my_set1.
my_set1 = set(list)
print(my_set1)

#10 Add Nucleotidase to the set.
my_set1.add('Nucleotidase')
print(my_set1)

#11 Remove Summit from the set.
my_set1.remove('Summit')
print(my_set1)

#12 Make another set called my_set2 containing the following: Alias, Assist, Belfry, Sideboard, Soap, Balalaika, Persimmon.
my_set2 = ['Alias', 'Assist', 'Belfry', 'Sideboard', 'Soap', 'Balalaika', 'Persimmon']

#13 Find the elements that intersect the two sets.
my_intersection = my_set1.intersection(my_set2)
print(my_intersection)

#14 Find the elements unique to my_set2.
my_unique = my_set1.difference(my_set2)
print(my_unique)

#15 Combine my_set1 and my_set2.
combine_set = my_set1.union(my_set2)
print(combine_set)

#16 Assign a = 16653509 and b = 2448111 and determine if the values are equal.
a = 16653509
b = 2448111
print(a == b)

#17 Use a comparison or logic operator to determine which is greater.
IsGreaterThan = a > b
print(IsGreaterThan)

IsLesserThan = a < b
print(IsLesserThan)
