# Create a function that adds two numbers and prints the sum of them.\n",
def function1(first,second):
    c = first + second
    print("The result of ",first , " + ", second , " is: ", c)

function1(10,20)


# Create a function that multiplies two provided variables
# Use a return statement with no variable assigned to it and test output of the function.
def function2(first,second):
    c = first * second
    print("The result of ",first , " multiplied by ", second , " is: ", c)
    return c

output = function2(10,12)
print("The value of 'output' is: ",output)


# Create a function that multiplies two provided variables and returns the result.
# Provide the values using keyboard input.
def function4():
    first = int(input("The first number is: "))
    second = int(input("The second number is: "))
    c = first * second
    print("The result of ",first , " multiplied by ", second , " is: ", c)
    return c

output = function4()
print("The value of 'output' is: ",output)


# Create a function that multiplies two provided variables and returns the result.\n",
# Include default values for the parameters and a docstring\n",
def function5(first = 0, second = 0):
    ''' function5 docstring
    This function takes two numbers and multiplies them to give a result.
    The output is returned after the function is finished.
    @param first
    @param second
    @return: The result of multiplying a and b
    '''
    c = first * second
    print("The result of ",first , " multiplied by ", second , " is: ", c)
    return c

output = function5(second=10,first=12)
print("The value of 'output' is: ",output)
print(function5.__doc__)























