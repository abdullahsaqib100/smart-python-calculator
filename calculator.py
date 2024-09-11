# Function to add two values entered by the user

def add (x,y):
    return (x + y)

# Function to subtract two values entered by the user

def subtract (x,y):
    return (x - y)

# Function to multiply two values entered by the user

def multiply (x,y):
    return (x * y)

# Function to divide two values entered by the user

def divide (x,y):    
    if y == 0:        # If y values entered by user is 0, it will return this message
        return "Error! You are dividing a number by zero"   
    return (x / y)

# Function to claculate the %age of two vlaues entered by the user

def percentage (x,y):
    return (x /y) * 100

# Creating Main function, that will show all the operations which a user can perform on this calculator by entering its number.

def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")

# Create an choise variable inside calculator function (created above)to pick a choise(operation he wants to perform) from the user as an input.

    choise = input("Enter choise (1/2/3/4/5): ")

# Created two variables to store the two values(numbers) upon which user weants to perform that above selected operation.

    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

# Used conditional statements, to perform selected choises/opeartions on the user entered numbers above

    if choise == "1" :
        print(f" {num1} + {num2} = {add (num1 , num2)}")

    elif choise == "2" :
        print(f" {num1} - {num2} = {subtract (num1, num2)}")

    elif choise == "3" :
        print(f" {num1} * {num2} = {multiply (num1, num2)}")

    elif choise == "4" :
        print(f" {num1} / {num2} = {divide (num1, num2)}")

    elif choise == "5" :
        print(f" The % of {num1} and {num2} is {percentage (num1 , num2)}")

    else:
        print("You have entered and invalid choise. Please select an valid choise & Try Again")

# writes the main fuction name to run it and to use calcultor

calculator()