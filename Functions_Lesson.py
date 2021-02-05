##Computers and Python
##Functions

#Four reasons to use functions
#1.Organize your code into “paragraphs”. Capture a complete thought and “name it”
#2.Don’t repeat yourself - make it work once and then reuse it
#3.If something gets too long or complex, break it up into logical chunks and put those chunks in functions
#4.Make a library of common stuff that you do over and over - perhaps share this with your friends...

#For the following function..
#argument:3,4
#parameter: a, b
#results: 7
import math
def add_two(a, b):
    x = a + b
    return x

add_two(3, 4)

def pyth(a,b):
    c = math.sqrt(a**2 + b**2)
    return c

def tax(price):
    x = price * 1.15
    return x
