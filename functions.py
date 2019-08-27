# problem1
# create function
def printNumbers():
    for x in range(-25, 21, 1):
        print(x)
# calling function
printNumbers()

# problem2
var1 = input("Enter Password  ")
var2 = input("Confirm Password  ")
def checkPassword(var1,var2):
    if var1 == var2:
        return "true"
    else:
        return "false"
print(checkPassword(var1, var2))

# problem3
def evenOrOdd(num):
    
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
        
num = int(input("enter a number.  "))
# evenOrOdd(num)
print(evenOrOdd(num))

# Problem4
def problem4():
    greet("hello")

# def greet():