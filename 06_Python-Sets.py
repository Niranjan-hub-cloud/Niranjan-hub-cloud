# Databricks notebook source
# MAGIC %md
# MAGIC ## SET
# MAGIC * It is Mutable collection.
# MAGIC * If we want to represent a group of unique values as a single entity then we should go for set. 
# MAGIC * Duplicates are not allowed. 
# MAGIC * Indexing and slicing not allowed for the set
# MAGIC * Set objects are mutable
# MAGIC * Same like list
# MAGIC * We can represent set elements within curly braces and with comma seperation 
# MAGIC * Example: {1,2,3,45,6}

# COMMAND ----------

s1={10,20,30,40,10,10,10,10}
print(s1)

print(type(s1))
#print(type(lst))


# COMMAND ----------

# MAGIC %md
# MAGIC how to remove duplicates from list

# COMMAND ----------

#convert any sequence to set
lst = [10,20,30,40,10,20,10]
print(lst)
s=set(lst)
print(s)
print(type(s))

# COMMAND ----------

#add: wil add element at first
s={10,20,30}
s.add(40);
print(s)

# COMMAND ----------

# MAGIC %md
# MAGIC * We can use add() to add individual item to the Set,where as we can use update() function 
# MAGIC to add multiple items to Set.  
# MAGIC * add() function can take only one argument where as update()  function 
# MAGIC can take any number of arguments but all arguments should be iterable objects. 

# COMMAND ----------

lst={1,3,4}
lst2=lst.update(10)

# COMMAND ----------

#example
s={10,20,30}
lst=[40,50,60,10]
s.update(lst,range(5))
print(s)  

# COMMAND ----------

#remove
It removes specified element from the set. 
If the specified element not present in the Set then we will get KeyError 

# COMMAND ----------

s={40,10,30,20,50}
s.remove(301) 
print(s)


# COMMAND ----------

#discard: same as remove but will not give error if element not found.
s={10,20,30} 
s.discard(300) 
print(s)

# COMMAND ----------

#clear

s={10,20,30}
print(s)
s.clear()
print(s) 

# COMMAND ----------



# COMMAND ----------

#union = x.union(y)  or     x|y
x={10,20,30,40} 
y={30,40,50,60} 
print(x.union(y))
#print(x|y) 



# COMMAND ----------

#intersection - x.intersection(y)   or   x&y 
#Returns common elements present in both x and y 
x={10,20,30,40} 
y={30,40,50,60} 
print(x.intersection(y))

# COMMAND ----------

#x.difference(y)  or  x-y returns the elements present in x but not in y 

x={10,20,30,40} 
y={30,40,50,60} 
#print(x.difference(y))   
#print(x-y) 
print(y-x)  

# COMMAND ----------

# Creating new collection retaining duplicates using 2 sets
s1 = {'2013-07-25 00:00:00.0', '2013-07-26 00:00:00.0', '2014-01-25 00:00:00.0'}
s2 = {'2013-08-25 00:00:00.0', '2013-08-26 00:00:00.0', '2014-01-25 00:00:00.0'}
s1.union(s2)

# COMMAND ----------

s={1,2,3,4,5}
print(s[0])

# COMMAND ----------


