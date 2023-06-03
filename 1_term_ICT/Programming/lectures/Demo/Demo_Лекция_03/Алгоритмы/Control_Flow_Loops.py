# # Lesson 3.
# # # Control Flow with Decisions and Loops

# True и False это 1 и 0:

a = True + 3
b = False + 3
print(a,b)          # 4 3


# Что является False?:

print(bool(-5), bool(0),bool("0"),bool(""),bool([]))  # True False True False False


# Using an if statement to find out if a variable is equal to 100
int1 = 50
if int1 == 100:
    print("The variable is equal to 100.")
else: print("The variable is not equal to 100.")


# Using an if statement to compare a variable to multiple values
int1 = 14
if int1 == 10: print("The variable is equal to 10")
elif int1 == 9: print("The variable is equal to 9")
elif int1 == 8: print("The variable is equal to 8")
elif int1 == 7: print("The variable is equal to 7")
elif int1 == 6: print("The variable is equal to 6")
elif int1 == 5: print("The variable is equal to 5")
elif int1 == 4: print("The variable is equal to 4")
elif int1 == 3: print("The variable is equal to 3")
elif int1 == 2: print("The variable is equal to 2")
elif int1 == 1: print("The variable is equal to 1")
else: print("The variable is not between 1 and 10")


# Using an if statement to print multiple statements
cost = 101
if cost >= 100: 
    print("You qualify for a 10% discount on a future purchase.")
    print("Please go to customer service for your discount card.")
else: 
    print("Thank you for shopping at our store.")
    print("Your purchase will be added to your rewards card.")



a = "чет" if 10 % 2 == 0 else "нечет"
print(a)


""" for

for expression in iterable:  # Для каждого элемента 'expression' из 'iterable'
    for_suite                # выполняется 'for_suite'
else:                        # (else - 0 или 1)
    else_suite               # Выполняется, если не было прерывания цикла
"""

# In[6]:


# Using a for statement to print the values in a list
clothes = ['shirts','pants','socks','hats','glasses','shoes']
for i in clothes:
    print(i)     # тело цикла
print(clothes)   # уже не тело цикла


# Using the for and continue statements.  Test the code by changing continue to break.
clothes = ['shirts','pants','socks','hats','glasses','shoes']
for i in clothes:
    if i == 'hats': continue
    print(i)


# Using the for and break statements.  Test the code by changing continue to break.
clothes = ['shirts','pants','socks','hats','glasses','shoes']
for i in clothes:
    if i == 'hats': break
    print(i)
else:
    print("Выведен полный список") # выполняется, если не использовался break


# Using a for statement to modify the values in a list
list1 = [2,4,6,8,10]
print("The old list1 is: ", list1)
for i in range(len(list1)):    # доступ к каждому элементу с помощью функции range([начало,] конец[, шаг])
    list1[i] = list1[i] * 3
print("The new list1 is: ", list1)


# Using a for statement to parse a dictionary
dict1 = {'FirstName':'William','LastName':'Robinson','Age':24}
for i in dict1:
    print(i)


""" while

while logical_expression:  # Если условие истинно, выполняется 'while_suite'
    while_suite            # После выполнения, происходит возврат к проверке
else:                      # (else - 0 или 1)
    else_suite             # Выполняется, если не было прерывания цикла
"""

# Using a while statement to do a looping operation 10 times
count = 1
while count < 11:
    print("The value of the variable is: ", count)
    count += 1
else:
    print("Не было прерываний цикла")


# Using the while and break statements.  Test the code by changing break to continue (infinite loop).
count = 1
while count < 11:
    if count == 5: break
    print("The value of the variable is: ", count)
    count += 1
else:
    print("Не было прерываний цикла")


# Using a while statement to continue indefinitely until a specified value is entered
count = 1
while count != 0:
    print("Enter the number 0 to end the loop.")
    count = int(input("Enter a number: "))
print("Count is equal to: ", count)


# Using a while statement with else
count = 10
while count > 1:
    print("Count is greater than 1. (",count,")")
    count -= 1
else: print("Count is less than or equal to 1")

