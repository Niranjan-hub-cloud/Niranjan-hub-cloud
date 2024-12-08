# Databricks notebook source
# MAGIC %md
# MAGIC ## Strings

# COMMAND ----------

The most commonly used object in any project and in any programming,  language is String only.
Hence we should aware complete information about String data type. 
Any sequence of characters within either single quotes or double quotes is considered as a String. 
Example:
s='abc' 
s="ABC" 
s='''ABC'''

# COMMAND ----------

s1='abc' 
s2="ABC" 
s3='''ABC'''
print(s1)
print(s2)
print(s3)
print(type(s1))

# COMMAND ----------

name='Bigdata'
print(name)
print(type(name))

# COMMAND ----------

name='Bigdata'
print(name)
lang="scala"
print(lang)
city='''bangalore'''
print(city)
car="""Hundai"""
print(car)
desc="""I love working on Hadoop technology
and Spark and Python"""
print(desc)


# COMMAND ----------

name="BidataTrends"
print(name)
print(type(name))
print(id(name))

#forwardindex
print(name[0])
print(name[1])
#print(name[2])
#print(name[3])
#print(name[4])
#print(name[5])

# COMMAND ----------

#negetive index
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

# COMMAND ----------

s = 'Hadoop'
print('d' in s)
print('z' in s)


# COMMAND ----------

#Slice

a="PYTHONLANGUAGE"
print(a[0:8])
print(a[8:12])
print(a[-8:-5])


# COMMAND ----------

#Strings can be concated using + operator
c="Hadoop"
w="Developer"
print(c+' '+w)


# COMMAND ----------

#String multiplication
a='ssr'
#print(a*2)
#String is immutable object we cannot replace or alter existing string object
s="ABCDEF"
print(s)
print(id(s))
c=s+"DD"
print(c)
print(id(c))


# COMMAND ----------

#String functions
#Capitalize(): It wiill convert first leeter into uppper
s="hadoop"
s.capitalize()

# COMMAND ----------

a="python hadoop"
print(a.title())

#IsLower
#IsUpper
#lower
#upper
#len() = it will count no of chanracters in string
#Count =  counts the noof occarances
#find= This will find the index position of specific character
#example:
str1="Spark Developer"
str2=str1.find('D')

print(str2)


# COMMAND ----------


#split= It will split the string into multiple strings
a="Spark Developer"
str4=a.split()
print(type(str4))
print(a.split())



# COMMAND ----------

b="Hadoop.Developer.Google"
c=b.split(".")
print(c)
print(type(c))


# COMMAND ----------

#Removing spaces from the string: 
We can use the following 3 methods 
 
1. rstrip()===>To remove spaces at right hand side 
2. lstrip()===>To remove spaces at left hand side 
3. strip() ==>To remove spaces both sides


# COMMAND ----------

city=input("Enter your city Name:")
scity=city.strip()
if scity=='Hyderabad':
    print("Capital of Telangana")
elif scity=='Chennai':
    print("Capital of Tamil")
elif scity=="Bangalore":
    print("Capital of Karnataka")
else:
    print("your entered city is invalid")


# COMMAND ----------

#find():

'''Returns index of first occurrence of the given substring. 
If it is not available then we will get -1 '''
 
s="Learning Python is very easy" 
print(s.find("Python"))   
print(s.find("Java"))   
print(s.find("r"))
print(s.rfind("r"))


# COMMAND ----------

#example2:
#s.find(substring,begin,end) 
s="bigdatatrends"   
print(s.find('a'))     
print(s.find('a',7,15))    
print(s.find('d',7,15))

# COMMAND ----------

#example:3
s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,7)) 


# COMMAND ----------

#replace:

Replace:

Syntax:
s.replace(oldstring,newstring) 
 
inside s, every occurrence of old string will be replaced with new string.

# COMMAND ----------

#example:

s="Learning Python is very difficult" 
s1=s.replace("difficult","easy") 
print(s1)


# COMMAND ----------

#Joining of Strings: 
#We can join a group of strings(list or tuple) wrt the given seperator. 
s=seperator.join(group of strings) 

# COMMAND ----------

#example1:
t=('Java','Scala','Python') 
s='-'.join(t) 
print(s) 
 


# COMMAND ----------

#example2:
lst=['hyderabad','singapore','london','dubai']
s=':'.join(lst)
print(s) 


# COMMAND ----------

s='learning Python is very easy' 
print(s.startswith('learning')) 
print(s.endswith('learning')) 
print(s.endswith('easy'))

# COMMAND ----------

isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to 9 )  
isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)  
isdigit(): Returns True if all characters are digits only( 0 to 9) 
islower(): Returns True if all characters are lower case alphabet symbols 
isupper(): Returns True if all characters are upper case aplhabet symbols 
istitle(): Returns True if string is in title case 
isspace(): Returns True if string contains only spaces 

# COMMAND ----------

print('Azure123'.isalnum())  
print('Python'.isalpha())  
print('ABC123'.isalpha())    
print('asddee'.isdigit())   
print('786786'.isdigit())   
print('abc'.islower())  
print('Abc'.islower())  
print('abc123'.islower()) 
print('ABC'.isupper())   
print('Learning python is Easy'.istitle())
print('Learning Python Is Easy'.istitle())
print('    '.isspace()) 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Formatting the Strings: 
# MAGIC We can format the strings with variable values by using replacement operator {} and format() method. 

# COMMAND ----------

#example:
name='VENKAT' 
salary=10000 
age=35 
print("{} 's salary is {} and his age is {}".format(name,salary,age)) 
#print("{0} 's salary is {1} and his age is {2}".format(name,salary,age)) 
#print("{z} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name)) 


# COMMAND ----------

#Reverse of String
s = input("Enter Some String:")
#Method1
print(s[::-1])





# COMMAND ----------

#method2
print(''.join(reversed(s)))

# COMMAND ----------

#Method3
s=input("Enter Some String:")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
    print(target)

# COMMAND ----------

'''Write a program to print characters at odd position and even position for the given String? '''

s=input("Enter Some String:") 
print("Characters at Even Position:",s[0::2]) 
print("Characters at Odd Position:",s[1::2]) 

# COMMAND ----------

#exatra examples
myString = "Hello"

#print first Character
print(myString[0])

#print last character using negative indexing
print(myString[-1])

#slicing 2nd to 5th character
print(myString[2:5])

# COMMAND ----------

#example:
s1 = "Hello "
s2 = "SSR"

#concatenation of 2 strings
print(s1 + s2)

#repeat string n times
print(s1 * 3)

# COMMAND ----------

s1 = "Bad morning"

s2 = s1.replace("Bad", "Good")

print(s1)
print(s2)

# COMMAND ----------

myStr = "Madam"

#convert entire string to either lower or upper
myStr = myStr.lower()

#reverse string
revStr = reversed(myStr)

#check if the string is equal to its reverse
if list(myStr) == list(revStr):
    print("Given String is palindrome")
else:
    print("Given String is not palindrome")

