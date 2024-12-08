# Databricks notebook source
# MAGIC %md
# MAGIC # Collections

# COMMAND ----------

# MAGIC %md
# MAGIC ## List in Python:
# MAGIC
# MAGIC * Group of homogenous elements.
# MAGIC
# MAGIC * There can be duplicates in the list.
# MAGIC
# MAGIC * list can be created by enclosing elements in [] - example [1, 2, 3, 4].
# MAGIC
# MAGIC * Empty list can be initialized using [] or list().
# MAGIC
# MAGIC * List is mutable collection

# COMMAND ----------

lst=[1,3,5,6,7,9]
print(lst)
print(type(lst))

# COMMAND ----------

names=["Sankar","abc","ertt"]
ages=[12,3,4,6,6]

nh=[10,90.7,'AB']
print(nh)

print(names)
print(type(names))
print(ages)

# COMMAND ----------

#Example:
lst = [1, 2, 3, 3, 4, 4]
print(lst)
print(type(lst))


# COMMAND ----------



# COMMAND ----------

lst2=[]
print(lst2)

# COMMAND ----------

help(lst)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Operators of Lists

# COMMAND ----------

# MAGIC %md
# MAGIC * IN: Check an element is exists or not in List
# MAGIC * LEN: To get number of elemnts in List
# MAGIC * SORTED : TO sort the data (Original order will not be touched). Typically, we assign the result of sorting to a new collection
# MAGIC * SUM : To perform total
# MAGIC * MIN: Minimun
# MAGIC * MAX: Maximum
# MAGIC * SPLIT: To split the list using separator
# MAGIC * COUNT: It will print occurances of the elements
# MAGIC * INDEX: To represent positions of elements in List
# MAGIC * APPEND: Add elements at the End. only single element can add at a time.
# MAGIC * INSERT: We can insert element at specific position
# MAGIC * EXTEND: Iterates over its argument and adding each element to the list and extending the list.
# MAGIC * REMOVE: It will remove specific element
# MAGIC * POP(): It will delete element from last position
# MAGIC * REVERSE: It will reverse the elemnts
# MAGIC * CLEAR: Deletes elemnts from List
# MAGIC * DEL(a:b): This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###  List Operations - Examples

# COMMAND ----------

# MAGIC %md
# MAGIC ####IN Operator

# COMMAND ----------


lst = [1, 2, 3, 5,4] 
#10 in lst
5 in lst

# COMMAND ----------

#length

print(len(lst))

# COMMAND ----------

#sorted
print(sorted(lst))

# COMMAND ----------

#split

str1="Python-Java-Course"
#print(type(str1))
lst=str1.split('-')  
print(lst)
print(type(lst))

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

#index
print(lst[0],lst[1])

# COMMAND ----------

lst=[10,20,30,40,50]
print(lst[0])
print(lst[4])

# COMMAND ----------

#slice
l1=[1,2,3,4,5,6,7,8,9,10]   
#print(l1[2:7:1])   
#print(l1[4::2])   
#print(l1[3:7])   
#print(l1[8:2:-1])   
print(l1[4:100])   

# COMMAND ----------

lst3=l1[4:100]
print(type(lst3))
print(lst3)

# COMMAND ----------

#for loop
n=[0,1,2,3,4,5,6,7,8,9,10]   

for n1 in n:
    print(n1, end='+')   

# COMMAND ----------

#for loop- even numbers
n=[0,1,2,3,4,5,6,7,8,9,10]   
for n1 in n:   
    if n1%2==0:   
        print(n1)   

# COMMAND ----------

#count- It will print occurances
n=[1,2,2,2,2,3,3]   
print(n.count(1))   
print(n.count(2))   
print(n.count(3))   
#print(n.count(4))

# COMMAND ----------

str2=['Azure','Python','SQL',10,10.5]
print(type(str2))

# COMMAND ----------

#append(): add elements at end
#mutable

list=[]   #empty list
list.append("A")   
list.append("B")   
list.append("C")   
list.append("C")   
print(list) 


# COMMAND ----------

#insert - at specific position
n=[1,2,3,4,5]   
n.insert(1,888)   
print(n)

# COMMAND ----------

# + also acct as insert only
l = n + [6]
print(l)

# COMMAND ----------

#extend
order1=["Lap","Mobile","TV"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)   
print(type(order1))


# COMMAND ----------

#remove
n=[10,20,100,30]
n.remove(10)
print(n)   

# COMMAND ----------

#pop():it will delete from last position
n=[10,20,30,40,50,60]
print(n.pop())
print(n.pop())
print(n)   

# COMMAND ----------

#reverse:
n=[10,20,30,40,50,60]
n.reverse()
print(n)

# COMMAND ----------

#not in:

lst=[100,200,300]
if 100 not in lst:
   print ("List is not having element with value 100")
else :
   print ("List is having element with value 100")

# COMMAND ----------

#max or min
print(max(lst))
print(min(lst))

# COMMAND ----------

#del
lt = ["apple", "banana", "cherry"]
del lt[0]
print(lt)

# COMMAND ----------


import keyword
keyword.kwlist

# COMMAND ----------

# MAGIC %md
# MAGIC ## Practical Examples
# MAGIC ### Question 1:
# MAGIC ### Access the name 'Maheer' from the list given below.

# COMMAND ----------


myList = [(2, 14, 'Maheer'), [2, 7], 'shaik']
print(myList[0][2])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 2:
# MAGIC #### We have a list of lists that contains several numbers. 
# MAGIC #### I want you to print the list whose sum of elements is the highest and also the lowest.
# MAGIC
# MAGIC lst = [[2, 1, 11], [4, 5, 7, 4], [8, 9, 10, 11], [19, 13, 7], [1, 5, 16]]

# COMMAND ----------


lst = [[2, 1, 11], [4, 5, 7, 4], [8, 9, 10, 11], [19, 30, 7], [1, 5, 0]]
print("The list with maximum sum of elements: ", max(lst, key = sum))
print("The list with minimum sum of elements: ", min(lst, key = sum))   


# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 3:
# MAGIC
# MAGIC Given below is the total marks of the 6 students in a class. Print the marks of the top 3 students from the given list.
# MAGIC
# MAGIC marks = [177, 160, 176, 183, 162, 170]

# COMMAND ----------


marks = [177, 160, 176, 183, 162, 170]

list_sort = sorted(marks)

print('Top Three Heights: ', list_sort[:-4:-1])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 4:
# MAGIC #Input list: list = ['A', 'B', 'C'] 
# MAGIC #Output: ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']

# COMMAND ----------

list1 = ['A', 'B', 'C']

new_list = [f'{x}{y}' for y in range(1, 4) for x in list1]
print(new_list)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 5:
# MAGIC We have a list given below. Add an item 2000 to the list, after the item 1000.
# MAGIC myList = [2, 8, [10, 20, [40, 60, [0, 1000], 30, 70], 80], 50]

# COMMAND ----------

myList = [2, 8, [10, 20, [40, 60, [0, 1000], 30, 70], 80], 50]

myList[2][2][2].append(2000)
print(myList)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 6:
# MAGIC We have two lists of numbers given below. I want you to create a third list by picking an odd-indexed element from the first list and even-indexed elements from the second list.
# MAGIC
# MAGIC list_1 = [5, 10, 15, 20, 25, 30, 35]
# MAGIC list_2 = [7, 14, 21, 28, 35, 42, 49]

# COMMAND ----------

list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]

list_3 = []

odd_index = list_1[1::2]
even_index = list_2[0::2]

list_3.extend(odd_index)
list_3.extend(even_index)

print(list_3)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 7:
# MAGIC Define a python function to print the longest word in the list of technologies given below.
# MAGIC
# MAGIC myList = ['Oracle', 'Data Science', 'Python', 'Machine Learning', 'Artificial Intelligence']
# MAGIC Output: Artificial Intelligence

# COMMAND ----------

lst1 = ['Oracle', 'Data Science', 'Python', 'Machine Learning', 'Artificial Intelligence']
def longest_word(*words):
    words_len = []
    
    for x in words:
        words_len.append((len(x), x))
    words_len.sort()
    
    return words_len[-1][1]
print(longest_word(*lst1))

# COMMAND ----------

# MAGIC %md
# MAGIC ### Question 8:
# MAGIC Write a python function to find the maximum of three numbers from the list given below, without using the built-in function max().
# MAGIC
# MAGIC numList = [10, 12, 17]

# COMMAND ----------

numList = [10, 12, 17]

def max_two(a, b):
    if a > b:
        return a
    return b

def max_three(a, b, c):
    return max_two(a, max_two(b, c))

print(max_three(*numList))

# COMMAND ----------

# MAGIC %md
# MAGIC
