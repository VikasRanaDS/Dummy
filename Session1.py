#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# Let's have a look at Python as a language and what features does it bring to be among the top 3 coding languages in the world.
# 

# In[ ]:


# 1. Unlike other languages Python program works on an Interpreter so to run a code all you have to do is type it out
print("Welcome to upGrad")


# In[ ]:


# 2. Python language runs line by line, so incase you want to update a piece of code all you have to do is 
#    update the line let's see how -


# In[ ]:


#Imaginary giraffe
print("O    ")
print("|    ")
print("|____")
print(" ||||")
print(" ||||")


# In[ ]:


#Let's add another print statement 
print("$" * 3)


# Now let's see what happened here  - 
# 
# Any character whether it be numeric or text enclosed within " " or ' '  gets considered as a string; 
# 
# A string is a data type which contains a series of characters
# 
# Just like string, there are numerous types of variables in Python; let's have a look
# 

# <h2 style="color:Brown"> Variables</h2>
# Python variables are a container that can store any type of value and of any particular size.
# Unlike other languages such as C, Java - Variables in Python don't need initialization. Let's create a variable to see how do they work 
# 
# 
# 
# 

# 

# In[ ]:


var1 = "Mike"
print(var1)


# In[ ]:


var2 = 6
print(var2)


# Now that we know how to store a variable in Python let's try getting input from a user and storing it in Python

# In[ ]:


#To get a input from a user we would use the 'input' function


# In[ ]:


number = input("What's your favourite number? ")
print(number)


# In[ ]:


#Let's try taking adding a string to the answer received
name = input("Enter your name : ")
print("Welcome", name)


# In[ ]:


#That was helpful, could I also perform operation on input received?
age = input("Enter your age : ")
print("You are " , age*12 , " months old")


# In[ ]:


age = input("enter your age ")
age = int(age)
print("You are " , age*12 , " months old")
#Changing the the of variables type is called typecasting


# <h2 style="color:Brown"> How to find the Data Type for a variables in Python
# 

# Here in the below piece of code you can see that we have assigned each variable with a particular value and use the type method we can check the datatype of the variable

# In[ ]:


integer_num = 1
floating_num = 1.3
string = 'Mike'
boolean = True

print (type(integer_num))
print (type(floating_num))
print (type(string))
print (type(boolean))


# - Type Casting in Python

# In[ ]:


Now let us try taking an 
a = 1
print ( bool(a))
print ( float(a))
print ( str(a))


# <h2 style="color:Brown"> Arithmatic Operations

# In[ ]:


#
a = 6
b = 7
print("Addition  = ", a + b)  
print("Substraction = ", a - b) 
print("Multiplication = ", a * b) 
print("Division = ", a / b)
print("Floor Division = ", a // b) 
print("Modulus or remainder",a % b) 
print("Exponential = ", a ** b)


# Now if you recall that the mathematical  operators follow a precedence rule called PEDMAS -
# Wherein the fist P is parenthesis, then it's E for exponents, M for multiplication, then D for division, A for addition and finally S for subtraction.
# 
# 
# Reference - [Python operator precedence](https://docs.python.org/3.7/reference/expressions.html?#operator-precedence)
# 

# In[ ]:


print((4 * 5) - 9 + 6 / 7)


# <h2 style="color:Brown"> String Operations

# We should look at strings as a banner where multiple characters are linked together. The string data is an immutable type which means it cannot be modified.

# In[ ]:


#Whenever we are assigning a char or string we use '' which represents a character
c = 'z'
d = 'Mike'
#You can also use " " double quotes instead of single quotes for strings
e = "John"


# In[ ]:


#Now when we want to include words with a single quote such as "didn't", "I'll".. we might end up with a error
print('I didn't know that')



# In[ ]:


#Now to solve this we can use an escape character like 
print('I didn\'t know that')


# In[ ]:


# Or we can use double quotes
print("I didn't know that")


# In[ ]:


#Now that '\' escape character which we saw earlier can also be used for other stuff like adding a new line
print("Hi Bob \n\nHow are you?")


# Now apart adding new lines to a string we can also add another to a pre-existing string, let's see how -
# 
# ###String Concatenation
# 

# In[ ]:


#Let's try building a system that could ask for flavour, and the type of desert user wants
flavour=input("What flavour would you like ")
dessert_type=input("What type of dessert would you like ")
print("You have ordered", flavour+"-"+dessert_type)


# Congrats on building a simple app using input and string functions. Let's take a step ahead and learn more about string manipulation
# 
# 

# ##String Manipulation

# #### Indexing In Strings <br>
# - Forward indexing starts with 0
# - Reverse indexing starts with the last character as -1 in a python string
# - Strings are immutable which, means they cannot be changed once created.
# - Strings can be modified by slicing a part of it and concatenating with another
# 

# In[ ]:


# Len() function
string = "I have not failed. I’ve just found 10,000 ways that won’t work. – Thomas A. Edison"
len(string)


# In[ ]:


#Accessing first character
string[-82]


# In[ ]:


#Accessing last character using negative indexing
string[-1] 


# In[ ]:


# Trying to change the character at index 2
string[2] = 't'


# In[ ]:


# Changing the entire string or say changing the label of it
string = 'I have not failed. I’ve just found 10,000 ways that won’t work.” – Einstien'
print (string)


# #### Slicing In Strings
# - string[start:end:step]

# In[ ]:


#slicing by specifying start and end index
statement = "I have not failed. I’ve just found 10,000 ways that won’t work. – Thomas A. Edison"
sliced_statement = statement[0:64]
print(sliced_statement)


# In[ ]:


batch = "5 girls 3 boys in a class"
girls = batch[ :8]
print(girls)

print(batch[ 8: ])


# In[ ]:


# Membership 
String = "John! Did you attend the conference on advanced machine learning"
print( 'Lincoln' in String)
print ( 'Behzad' not in String)


# #### String methods
# - upper()
# - lower()
# - strip()
# - count(substring,begin,end)
# - https://docs.python.org/3.7/library/stdtypes.html#string-methods

# In[ ]:


# upper() 
small = "i am upper cased"
print(small.upper())


# In[ ]:


# lower() 
large = "I AM LOWER CASED"
print(large.lower())


# In[ ]:


# rstrip () function
some_sentence = "There is a space at the end    "
print(some_sentence)
print(some_sentence.rstrip())


# In[ ]:


increment = '4%'
print(increment.rstrip('%')) 


# In[ ]:


# lstrip() function
start = "   There is space at the start"
print(start)
print(start.lstrip())


# In[ ]:


# strip() function 
spaces = "   Trim whitespaces  "
print(spaces)
print(spaces.strip())


# In[ ]:


num_with_chars = '******444#######'
print(num_with_chars.rstrip('#').lstrip('*'))


# In[ ]:


#count() Method
string = "This is a sample sentence"
print(string.count('i'))
print(string.count('i',5))


# In[ ]:


#r/R It is used to specify the raw string.% It is used to perform string formatting.

A = "Data"
B = "Analysis"
C = "Pandas"

print("{0} {1} using {2}".format(A,B,C))


# In[ ]:


#Now there are a plenty of other string operations available in Python you could explore those using - 
help(str)
#Ignore the methods with a double underscore, for now, those are called the magic methods and we have seen enough magic for the day to be a Python Wizard!!

