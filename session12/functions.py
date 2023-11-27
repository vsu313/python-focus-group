#!/usr/bin/env python3

# Create a function
def greeting():
    print("Hello, world!")
    
# Call function
greeting()


# Create a function with argument 'some_string'
def add_underscore(some_string):
    new_string = some_string + "_"
    print(new_string)

# Call function
add_underscore("Viki")


def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

add_numbers(3, 7)


# Create a function that prints the first letter (initial) of each input name
def first_letters(*names):
    for name in names:
        print(name[0])

first_letters("Bijoy", "Helen", "Miley", "Roxanna")


def my_kids(child3, child2, child1):
    print("The youngest child is " + child3)
    
my_kids("Emily", "Tobias", "Linus")

my_kids(child1 = "Emily", child2 = "Tobias", child3 = "Linus") 


def my_home(country = "USA"):
    print("I am from " + country)
    
my_home("Sweden")
my_home("Lebanon")
my_home()


def associate_ages(a_dictionary):
    for name, age in a_dictionary.items():
        print(f'{name} is {age} years old.')

ages = {"Viki": 25, "Logan": 25, "Osman": 30}
associate_ages(ages)


# Original
print("Here, we are testing the original function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var)

# With Return
print("Here, we are testing the rewritten function")
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
    
my_var = add_numbers(3, 7)
print("My variable: ", my_var)


# Original
def add_numbers(number1, number2):
    my_sum = number1 + number2
    print(my_sum)

# With Return
def add_numbers(number1, number2):
    my_sum = number1 + number2
    return my_sum
    
    
def empty_function():
    pass

a = empty_function()
print(a)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)


# Create function with a description
def add1(a):
    """
    Add 1 to a
    """
    b = a + 1
    return b

# Execute function
add1(5)


help(add1)