# Databricks notebook source
# MAGIC %md
# MAGIC #1. History of Python:
# MAGIC **Under the leadership of “Andrew Stuart Tanenbaum” a group of employees developed Distributed Operating System. They used ABC scripting language. The ABC scripting language Is simple and easy to work. “Guido Van Rossum” is a member in that group. In the Christmas holidays, he started developing a new language to be simple and easy compared to ABC. Finally, he developed python in National Research Institute for Mathematics and Computer Science in Netherlands in 1989 and named as “PYTHON”**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC . Python 1.0 was released in 1994
# MAGIC
# MAGIC •	Python 2.0 was released in 2000 (python2)
# MAGIC
# MAGIC •	Python 3.0 was released in 2008 (python3)
# MAGIC
# MAGIC •	Python is a general-purpose high-level programming language
# MAGIC
# MAGIC •	Rossum has taken concepts from different programming languages
# MAGIC
# MAGIC •	Scripting based applications will run by interpreter and not required explicit compilation
# MAGIC
# MAGIC •	Examples of scripting languages are shell scripting, python, Perl, ruby etc. all these languages run by interpreter. So, we called them as scripting languages.
# MAGIC
# MAGIC •	Programming language bases applications will run by compiler
# MAGIC
# MAGIC •	Programming languages cannot run without compilation
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # 2. Different languages which are used to develop python
# MAGIC
# MAGIC * Procedural programing language: c
# MAGIC
# MAGIC •	Object Orient Programming languages Java and C++
# MAGIC
# MAGIC •	Scripting languages: Perl and shell scripting
# MAGIC
# MAGIC •	Modular programming: Module3

# COMMAND ----------

# MAGIC %md
# MAGIC # 3. Features of Python
# MAGIC **
# MAGIC •	Python is simple and powerful language. The syntax of python is very simple and easy to remember
# MAGIC •	Reading a python is same as reading English
# MAGIC
# MAGIC •	Using python, developers can easily express their business logic within a smaller number of lines
# MAGIC
# MAGIC •	Python has few keywords, simple structure and clearly defined syntax. 
# MAGIC
# MAGIC •	Python has rich libraries to support Web applications, Scientific and other types of applications
# MAGIC
# MAGIC •	Python is portable
# MAGIC
# MAGIC •	The memory allocation will happen dynamically when you run the application
# MAGIC
# MAGIC •	Interactive language
# MAGIC
# MAGIC •	Supports all major commercial databases
# MAGIC
# MAGIC •	Supports GUI applications
# MAGIC
# MAGIC •	Support Gaming applications
# MAGIC
# MAGIC •	Supports scientific applications
# MAGIC
# MAGIC •	Network applications
# MAGIC
# MAGIC •	Animation apps
# MAGIC **

# COMMAND ----------

# MAGIC %md
# MAGIC # 4.Python Identifiers
# MAGIC •	A python identifier is a name used to identify a variable, function, class, module.
# MAGIC •	An identifier will start with A-Z or a-z or 0-9. 
# MAGIC •	Reserve keywords cannot used as identifiers

# COMMAND ----------

# MAGIC %md
# MAGIC # 5. Python Keywords
# MAGIC The keywords in python having predefined functionality. Keywords cannot be used as variables or constants.

# COMMAND ----------

#To see all the keywords:
import keyword
keyword.kwlist

# COMMAND ----------

# MAGIC %md
# MAGIC # 6. Variable Declaration
# MAGIC Here we can assign single vale or multiple values at a time.

# COMMAND ----------

a=10
b=20
c='Hadoop'
d="Scala"
e='''Python'''

print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(d))

# COMMAND ----------

#Another type of declaration

a,b,c = 100,20.5,"Maheer"

print(a)
print(type(a))
print(id(a))

print(b)
print(type(b))
print(id(b))

print(c)
print(type(c))
print(id(c))

# COMMAND ----------

#Another type of declaration

a=b=c="BigdataTrends"

print(a)
print(b)
print(c)

# COMMAND ----------

#Examples on variables

myname ="ABC"
myjob ="Software Developer"
car ='Maruthi Suzuki SCROSS'
cost =100000
## INR

print("my name is %s" %myname)
print("my job is %s"%myjob)
print("my fav car is %s"%car)
print("car cost is %d"%cost)

# COMMAND ----------

course='MCA'
fees =2000
print('course name is :',course)
print('course fees is :',fees)

# COMMAND ----------

Empno=37893
Ename = "ABC"
Job = "Hadoop Developer"
byhandsalary =1000
totalsalary=2000

tax=1000*10/100
hike =totalsalary*0.10
comm = 500
netsal=comm+byhandsalary
print("my name is", Ename, "He is super")
print("my total salary is",netsal)

# COMMAND ----------

# MAGIC %scala
# MAGIC val course="MCA"
# MAGIC val fees =2000
# MAGIC println("course name is :",course)
# MAGIC println("course fees is :",fees)
# MAGIC
