#!/usr/bin/env python
# coding: utf-8

# # Lesson 1
# ## Introduce Python variables, data types, operators and built-in commands
# 

# In[3]:


# Получение списка ключевых слов
import keyword
print(keyword.kwlist)


# In[2]:


# Получение списка встроенных идентификаторов
import builtins
print(dir(builtins))


# ### Типы данных

# In[12]:


a,b = True, False    # логический
print(type(a), type(b))
print(int(a), int(b))
print(bool(10), bool(-10), bool(0))


# In[23]:


print(type(2 + 3j))
print(type([1,2,3,4])) # список
print(type((1,2,3,4))) # кортеж
print(type(range(1,4))) # диапазон
print(type({"x":1, "y":2})) # словарь
print(type({"a", "b", "c"})) # множество


# In[34]:


# изменяемые типы - списки, словари
arr = [1,2,3,4,5,6]
print(arr, id(arr))
arr[0] = 11
print(arr, id(arr))
arr = [11,22,33,44,55,66]
print(arr, id(arr))


# In[20]:


# неизменяемые типы - числа, строки, кортежи, диапазоны
arr = (1,2,3,4,5,6)
# arr[0] = 11 # TypeError: 'tuple' object does not support item assignment
print(arr, id(arr))
arr = (7,8,9,10)
print(arr, id(arr))


# In[17]:


var1 = "Data Science is better than chocolate or ice cream."
print(var1, type(var1), id(var1))
var1 = 12
print(var1, type(var1), id(var1))


# In[38]:


string1 = "This is a string."
string2 = "  This is another string."
print(string1, id(string1))
string1 += string2
print(string1, id(string1))
string3 = string1 + string2
string3
print("The first sixteen (16) characters in string3 are: ", string3[0:16]) # получение среза


# In[6]:


integer1 = 5
float1 = 5.5
integer2 = integer1 + 20
print("Add two integer values: ", integer1 + integer2)
print("Multiply two integer values: ", integer1 * integer2)
print("Concatenate two integer values: ", str(integer1) + str(integer2))


# ### Особенности присваивания

# In[40]:


x = y = 10 # групповое присваивание
print(x,y,id(x),id(y),(x is y)) # две переменные ссылаются на один и тот же объект


# In[43]:


x = y = [1,2]
a = b = (1,2)
print(x,y,id(x),id(y),(x is y))
print(a,b,id(a),id(b),(a is b))
x[0] = 3
print(x,y,id(x),id(y),(x is y))


# In[49]:


x=2; y=2; z=2 
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z)) # кеширование малых целых чисел и строк
import sys
print(sys.getrefcount(2)) # количество ссылок на объект


# In[50]:


# позиционое присваивание
x, y, z = 1,2,3
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))


# In[54]:


x, y, z = "abc"
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))
x, y, z = (1,2,3)
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))
x, y, z = [11,22,33]
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))


# In[56]:


# * - присваивается список
x, y, *z = "qwertyuiop"
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))
x, *y, z = (1,2,3,4,5,6,7,8)
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))
*x, y, z = [11,22,33,44,55,66,77,88]
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))
x, y, *z = [111,222]
print(x,y,z,id(x),id(y),id(z),(x is y), (y is z))


# ### Проверка и преобразование типа данных

# In[1]:


a = 1
print(a,id(a), type(a))
a = "a"
print(a,id(a), type(a))


# In[2]:


s = "qwerty"
if isinstance(s,int):
    print("это целый тип")
if isinstance(s,str):
    print("Это строка")

# isdigit() - проверить, состоит ли строка из одних цифр 
print("asa".isdigit())  # False
print("102".isdigit())  # True

# isalpha() - проверить, состоит ли строка из одних букв
print("asa".isalpha())  # True

# isalnum() - проверить, состоит ли строка из букв или цифр
print("as10".isalnum())  # True

# In[5]:


a = int("22") # преобразует строку в целое
print(type(a))
a = str(22) # преобразует объект в строку
print(type(a))
a = list("12345qwert") # преобразует последовательность в список
print(a, type(a))
a = tuple("12345qwert") # преобразует последовательность в кортеж
print(a, type(a))


# In[7]:


# получение данных от пользователя
print("Enter two numbers to be added:")
n1 = input("Enter the first number:  ")
n2 = input("Enter the second number: ")
n3 = int(n1) + int(n2)
print(n1 + " plus " + n2 + " = ", n3)


# In[8]:


x = 1;
del x; # удаление переменной
print(x) # NameError: name 'x' is not defined


# In[4]:


help(str)


# In[7]:


# Get information about the attributes of a variable
dir(integer1)


# ### Кортежи и списки

# In[8]:


sequence1 = (0, 10,20,30,40,50,60,70,80,90,100) ; list1 = list(sequence1) ; list1[0] = 1
print("sequence1 values: ", sequence1)
print("list1 values: ", list1)
print("list1 multiplied by 2: ", list1 * 2)
print("The number of values in the list is:", len(list1))
list1


# In[ ]:


# Sort the list in reverse order
print("The last value output is: ", _)
print("list1 sorted in reverse order is: ", sorted(list1,reverse=True))


# In[ ]:


list1 = [1,2,3,4,5]
list1.append(6)
print(list1)
list1[0] = 0
list1[2] = 4
print(list1)


# In[ ]:


string1 = "0000000Please remove the zeros from this string.0000000" ; print(string1.strip('0'))


# In[ ]:


# Will generate errors.  Comment out the lines that have errors to run successfully  
str1 = "Test string."
print("str1 is: ", str1)
# print(int(str1))       # Cannot convert text-based string to integer
tuple1 = (1,2,3,4,5)
# tuple1.append(6)       # Cannot append to tuple
list1 = [1,2,3,4,5]
list1.append(6)
print("The first three (3) values in list1 are: ", list1[0:3])
print("All the values in list1 are: ", list1)


# In[ ]:


dict1 = {'name':'Carlos Santiago','age':'43','phone':'123-456-789'}
print("The data type of the dict1 variable is: ",type(dict1))
print("The phone number is: ",dict1['phone'])
display(dict1.keys())
dict1.values()


# In[ ]:


# Using help and dir
list1 = [82,8,23,97,92,44,17,39,11,12]
dir(list1)
help(list1.insert)
list1.insert(0,5)
help(list1.append)
list1.append(6)
help(list1.reverse)
list1.reverse()


# ### Команды

# In[14]:


get_ipython().system('pip list')


# In[ ]:


get_ipython().run_line_magic('lsmagic', '')


# In[9]:


get_ipython().run_cell_magic('time', '', 'string1 = "123456789"\nstring2 = "987654321"\nstring3 = "999999999"\ninteger1 = int(string1) * int(string2) * int(string3)\nprint(integer1)')


# ###  Операторы

# In[ ]:


# Test arithmetic operators
print(2 ** 4)
print(2 * 4)
print(2 + 4)
print(2 - 4)
print(2 / 4)
print(2 // 4)
print(2 % 4)


# In[9]:


print(0.3-0.1-0.1-0.1)


# In[ ]:


# Test comparison operators
print(2 < 4)
print(2 > 4)
print(2 != 4)
print(2 == 4)
print(2 <= 4)
print(2 >= 4)


# In[11]:


# Test bit operators
print(22 | 24)
print(21 & 41)
print(2 ^ 4)
print(21 << 4)
print(22 >> 2)
print(-12 >> 2)

