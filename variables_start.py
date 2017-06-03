#
# Example file for variables
#

# Declare a variable and initialize it
f = 0;
print f

# re-declaring the variable
f = "abc";
print f

# global vs local variables

def someFunction():
    global f
    f = "def"
    print f

someFunction()
print f

del f # delete a definition of the var previously declared
print f # error bc "f" was undefined
