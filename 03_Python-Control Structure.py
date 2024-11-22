# Databricks notebook source
# MAGIC %md
# MAGIC 1.if:
# MAGIC Syntax:
# MAGIC if condition : statement 
# MAGIC    
# MAGIC    (or) 
# MAGIC  
# MAGIC if condition :      
# MAGIC  statement-1      
# MAGIC  statement-2      
# MAGIC  statement-3
# MAGIC  
# MAGIC  
# MAGIC If condition is true then statements will be executed.

# COMMAND ----------

name = input("Enter Name:")
if name == "Maheer":
    print("Hello Maheer Good Morning")
    print("How are you!!!")


# COMMAND ----------

# MAGIC %md
# MAGIC 2) if-else: 
# MAGIC  
# MAGIC if condition : 
# MAGIC   Action-1 
# MAGIC else :      
# MAGIC   Action-2 
# MAGIC  
# MAGIC if condition is true then Action-1 will be executed otherwise Action-2 will be executed.

# COMMAND ----------

#Example
name=input("Enter Name:")
if name=="Python":
    print("Hello Python Good Morning")
else:
    print("Hello Guest Good Moring")
    print("How are you!!!")

# COMMAND ----------

# MAGIC %md
# MAGIC 3) if-elif-else: 
# MAGIC    Syntax: 
# MAGIC  
# MAGIC if condition1:     
# MAGIC  Action-1 
# MAGIC elif condition2:     
# MAGIC  Action-2 
# MAGIC elif condition3:     
# MAGIC  Action-3  
# MAGIC elif condition4:     
# MAGIC  Action-4     
# MAGIC ... 
# MAGIC ...
# MAGIC ...
# MAGIC else:     
# MAGIC Default Action
# MAGIC  

# COMMAND ----------

#Example:
name=input("Enter Your Name:")
if name=="Shakeer":
    print("He is Hadoop Developer")
elif name=="Anup":
    print("He is DB Developer")
elif name=="Madhavi":
    print("She is Manager")
else :
    print("Default case")


# COMMAND ----------

#Example2:
#Biggest number using if else

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
if n1>n2:
    print("Biggest Number is:",n1)
else :
    print("Biggest Number is:",n2)


# COMMAND ----------

#Example3:
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
n3 = int(input("Enter Third Number:"))
if n1 > n2 and n1 > n3:   
    print("Biggest Number is:", n1)
elif n2 > n3:
    print("Biggest Number is:", n2)
else:
    print("Biggest Number is:", n3)

# COMMAND ----------

#Write a program to check whether the given number is in between 1 and 100?
n=int(input("Enter Number:"))
if n>=1 and n<=10 :
     print("The number",n,"is in between 1 to 10")
else:
     print("The number",n,"is not in between 1 to 10")


# COMMAND ----------

#Example
n=int(input("Enter a digit from o to 9:"))   
if n==0 :   
    print("ZERO")   
elif n==1:   
    print("ONE")   
elif n==2:   
    print("TWO")   
elif n==3:   
    print("THREE")   
elif n==4:   
    print("FOUR")   
elif n==5:   
    print("FIVE")   
elif n==6:   
    print("SIX")   
elif n==7:   
    print("SEVEN")   
elif n==8:   
    print("EIGHT")   
elif n==9:   
    print("NINE")   
else:  
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")

# COMMAND ----------

# MAGIC %md
# MAGIC # for loop:

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC If we want to execute some action for every element present in 
# MAGIC some sequence(it may be string or collection)then we should go for loop. 
# MAGIC
# MAGIC Syntax: 
# MAGIC  
# MAGIC for x in sequence :    
# MAGIC  body 
# MAGIC  
# MAGIC where sequence can be string or any collection. Body will be executed for every element present in the sequence. 
# MAGIC

# COMMAND ----------

#Example:
 
#To print characters, present in the given string
s="Bangalore"
for x in s :
    print(x)

# COMMAND ----------

#Eg 3:  To print Hello 10 times 
for x in range(10) :
    print("Hello")  


# COMMAND ----------

print("Hello") 
print("Hello") 
print("Hello")
print("Hello") 
print("Hello") 
print("Hello") 
print("Hello") 
print("Hello") 

# COMMAND ----------

#Eg 4: To display  numbers from 0 to 9 
for x in range(10) :   
    print(x)

# COMMAND ----------

#Eg 5:  To display odd numbers from 0 to 20 
for x in range(21) :   
    if (x%2!=0):    
        print(x)   

# COMMAND ----------

#Example 6:  
#To display numbers from 10 to 1 in descending order 
for x in range(10,0,-1) : 
    print(x)  

# COMMAND ----------

# MAGIC %md
# MAGIC break:   
# MAGIC
# MAGIC We can use break statement inside loops to break loop execution based on some condition.
# MAGIC

# COMMAND ----------

#Example:
for i in range(10):
    if i == 7:
        print("processing is enough..plz break")
        break
    print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC 2) continue: 
# MAGIC  
# MAGIC We can use continue statement to skip current iteration and continue next iteration.

# COMMAND ----------

#Example:
#To print odd numbers in the range 0 to 9

for i in range(10):
    if i % 2 == 0:   
        continue
    print(i)

# COMMAND ----------

lst=[10,20,500,700,50,60]
for item in lst:
    if item>=500:
        #print("We cannot process this item :",item)
        continue   
    print(item)

# COMMAND ----------

#Example:
a = [10, 20, 0, 5, 0, 30]
for n in a:
    if n == 0:   \
    print("Hey how we can divide with zero..just skipping")
    continue
print("100/{} = {}".format(n, 100 / n))  

# COMMAND ----------

#loops with else block: 
 
#Inside loop execution, 
#if break statement not executed ,then only else part will be executed. else means  loop without break


#Example:

lst = [10, 20, 30, 40, 50,600]
for item in lst:
    if item >= 500:
        print("We cannot process this order",item)
        break
    print(item)
else:
    print("Congrats ...all items processed successfully")



# COMMAND ----------

#exAMPLE
b=[10,20,600,30,40,50]
for item in b:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)
else:
    print("Congrats ...all items processed successfully")


# COMMAND ----------

# MAGIC %md
# MAGIC pass statement: 
# MAGIC  
# MAGIC pass is a keyword in Python. 
# MAGIC In our programming syntactically if block is required which won't do anything then we can define that empty block with pass keyword. 
# MAGIC  
# MAGIC Pass:      
# MAGIC |- It is an empty statement      
# MAGIC |- It is null statement      
# MAGIC |- It won't do anything 
# MAGIC  
# MAGIC use case of pass:   
# MAGIC
# MAGIC Sometimes in the parent class we have to declare a function  with empty   body and child class responsible to provide proper implementation. Such type of empty body we can define by using pass keyword. (It is something like abstract method in java)    
# MAGIC Eg:   def m1(): pass 
# MAGIC
# MAGIC

# COMMAND ----------

for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass 

# COMMAND ----------

# MAGIC %md
# MAGIC del statement: 
# MAGIC  
# MAGIC del is a keyword in Python. 
# MAGIC After using a variable, it is highly recommended to delete that variable if it is no longer required,so that the corresponding object is eligible for Garbage Collection. We can delete variable by using del keyword.
# MAGIC

# COMMAND ----------

#Example:

x=10  
print(x)    
del x  
print(x)

