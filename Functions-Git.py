# 4.13.3: Greetings
# Riley Schippers
# 2.5.19


name = input(" What is your name???: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Riley Schippers
# 2.11.19

x = 10

def print_something():
    x = 3
    print  ('\n', x)

print('\n', x)
print_something()


# 4.13.6: Functions & Variables, Part 3
# Riley Schippers
# 2.18.19

def print_number(x):
    print(x)

print_number(13)
print_number(23)


# 4.14.4: Name & Age
#Riley Schippers
#2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is', name, 'and I am', str(age), 'years old!')

name_and_age('Mike', 33)
name_and_age('Zane', 18)


# 4.14.5: Default Parameter Values
# Riley Schippers
# 2.19.19

def print_two_number(x, y = 20):
    print('First number:', x)
    print('Second Number: ' + str(y))

print_two_number(34, 45)
print_two_number(78)


# 4.16.6 :Print Sum
#Riley Schippers
# 2.19.19

def print_sum(x, y):
    print(x + y)

print_sum(46,62)

# 4.16.3: Enter a Number using Try & Except
# Riley Schippers
# 2.20.19


try:
    my_num = int(input('Enter an Integer: '))
    print('Your number:', my_num)

except ValueError:
    print('\n''That was not an integer, off to gulag')

print_sum(46,62)

