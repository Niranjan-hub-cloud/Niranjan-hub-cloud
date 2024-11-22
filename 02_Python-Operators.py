# Databricks notebook source
# MAGIC %md
# MAGIC # 10. Operators in Python
# MAGIC
# MAGIC Operator is a symbol that performs certain operations. Python provides the following set of operators 
# MAGIC  
# MAGIC 1.  Arithmetic Operators 
# MAGIC 2.  Relational Operators or Comparison Operators 
# MAGIC 3.  Logical operators 
# MAGIC 4.  Bitwise operators 
# MAGIC 5.  Assignment operators 
# MAGIC 6.  Special operators

# COMMAND ----------

# MAGIC %md
# MAGIC ####1. Arithmatic Operators
# MAGIC + ==>Addition 
# MAGIC
# MAGIC - ==>Subtraction 
# MAGIC
# MAGIC * ==>Multiplication 
# MAGIC
# MAGIC / ==>Division operator 
# MAGIC
# MAGIC % ==>Modulo operator 
# MAGIC
# MAGIC // ==>Floor Division operator 
# MAGIC
# MAGIC ** ==>Exponent operator or power operator 
# MAGIC

# COMMAND ----------

#example
a=10   
b=20  
print('sum is',a+b)   
print('minus is',a-b)   
print('multiplication=',a*b)   
print('a/b=',a/b)   
print('a//b=',a//b)   
print('a%b=',a%b)   
print('a**b=',a**b)

# COMMAND ----------

s="ABC"   
a=33   
s1="Scala"   
s2="Python"   
print("Hello",s,"Your Age is", a)   
print("You are teaching",s1,"and",s2)


# COMMAND ----------

# MAGIC %md
# MAGIC ####2. Relational Operators
# MAGIC >
# MAGIC >=
# MAGIC <
# MAGIC <= 

# COMMAND ----------

#example:
a=100  
b=200   
print("a > b is ",a>b)   
print("a >= b is ",a>=b)   
print("a < b is ",a<b)   
print("a <= b is ",a<=b)   


# COMMAND ----------

#We can apply relational operators for str types also.

a="Hadoop"   
b="Spark"   
print("a > b is ",a>b)   
print("a >= b is ",a>=b)   
print("a < b is ",a<b)
print("a <= b is ",a<=b)


# COMMAND ----------

a=10   
b=20   
if(a>b):   
    print("a is greater than b")   
else:   
    print("a is not greater than b")    

# COMMAND ----------

# MAGIC %md
# MAGIC ####3. Equality Operators
# MAGIC ==
# MAGIC
# MAGIC !=
# MAGIC

# COMMAND ----------

#Example

10==20
#10<>20
100!=100
100==True
10=="Spark"  
"HADOOP"=="HADOOP"

# COMMAND ----------

# MAGIC
# MAGIC %md
# MAGIC ####4. Logical Operators
# MAGIC

# COMMAND ----------

print(True & True)  
print(10 & 5) 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Input and Output Statements:

# COMMAND ----------

# MAGIC %md
# MAGIC raw_input(): 
# MAGIC  
# MAGIC This function always reads the data from the keyboard in the form of String Format.  We must convert that string type to our required type by using the corresponding type casting methods. 
# MAGIC
# MAGIC input():  
# MAGIC   
# MAGIC input() function can be used to read data directly in our required format. We are not required to perform type casting. 

# COMMAND ----------

x=input("Enter Value")  
type(x) 

# COMMAND ----------

x=input("Enter First Number:")   
y=input("Enter Second Number:")   

i = int(x)  
j = int(y)   
print("The Sum:",i+j)   

# COMMAND ----------

x=int(input("Enter First Number:"))   
y=float(input("Enter Second Number:"))
print(type(x))
print(type(y))

# COMMAND ----------

print("The Sum:",int(input("Enter First Number:"))+int(input("Enter Second Number:")))   

# COMMAND ----------



# COMMAND ----------

#Write a program to read Employee data from the keyboard and print that data
eno=int(input("Enter Employee No:"))   
ename=input("Enter Employee Name:")   
esal=float(input("Enter Employee Salary:"))   
eaddr=input("Enter Employee Address:")   
married=bool(input("Employee Married ?[True|False]:"))   

print("Employee No :",eno)   
print("Employee Name :",ename)   
print("Employee Salary :",esal)   
print("Employee Address :",eaddr)   
print("Employee Married ? :",married)   

# COMMAND ----------

# MAGIC %md
# MAGIC ## Command Line Arguments:
# MAGIC
# MAGIC Argv is not Array it is a List. 
# MAGIC It is available sys Module. 
# MAGIC The Argument which are passing at the time of execution are called Command Line Arguments.
# MAGIC Within the Python Program this Command Line Arguments are available in argv. Which is present in SYS Module.
# MAGIC
# MAGIC Note: 
# MAGIC argv[0] represents Name of Program. But not first Command Line Argument. argv[1] represent First Command Line Argument.

# COMMAND ----------

#Write a Program to display Command Line Arguments?

print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv)
print("Command Line Arguments one by one:")

for x in argv:
    print(x)
#py test.py 10 20 30  

# COMMAND ----------

# MAGIC %md
# MAGIC * If both arguments are String type then + operator acts as concatenation operator. 
# MAGIC  
# MAGIC * If one argument is string type and second is any other type like int then we will get Error 
# MAGIC  
# MAGIC * If both arguments are number type then + operator acts as arithmetic addition operator
# MAGIC

# COMMAND ----------

#If both arguments are String type then + operator acts as concatenation operator. 
 
#If one argument is string type and second is any other type like int then we will get Error 
 
#If both arguments are number type then + operator acts as arithmetic addition operator


# COMMAND ----------

print("Hello"+"World")   
print("Hello","World")   

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

a,b,c=10,20,30   
print("The Values are :",a,b,c)   


# COMMAND ----------

#If we want output in the same line with space 
print("Hello",end=' ')   
print("Hadoop",end=' ')  
print("Spark")


# COMMAND ----------

s="ABC"   
a=33   
s1="Scala"   
s2="Python"   
print("Hello",s,"Your Age is", a)   
print("You are teaching",s1,"and",s2)

# COMMAND ----------

a=10   
b=20   
c=30   
print("a value is %i" %a)   
print("b  value is %d and c value is %d" %(b, c))

# COMMAND ----------

'''
%i====>int 
%d====>int 
%f=====>float 
%s======>String type 
'''

# COMMAND ----------

a=100    
b=200   
c=300   
print("a value is %i" %a)   
print("b  value is %d and c value is %d" %(b,c))


# COMMAND ----------

str="ABC"   
list=[10,20,30,40]   
print("Hello %s ...The List of Items are %s"  %(str,list))


# COMMAND ----------

name="RamCharan"
salary=10000
gf="Kajol"

print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
#print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z= gf))


# COMMAND ----------


