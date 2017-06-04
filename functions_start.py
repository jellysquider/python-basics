# -*- coding: utf-8 -*-
#
# Example file for working with functions
#


# define a function
def func1():
    print "I am a function"

func1()
print func1() # prints function and returns None
print func1  # error - the function is not invocked prints its hexadecimal address
# functions are objects  and it prints out the value of the func1 object

# function that takes arguments
def func2(arg1, arg2):
    print arg1, " ", arg2

func2(10,20)
print func2(10,20)

# function that returns a value
def cube(x):
    return x*x*x

print cube(3)

# function with default value for an arg
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

print power(2) # x is default 1
print power(2,3)
print power(x=3, num=2)

# fn with variable number of arg
def multi_add(*args): # a star – pass a variable number of agrs
    result = 0;
    for x in args:
        result = result + x
    return result

print multi_add(4,5,10,4,10)
