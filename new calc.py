print("Select the operation to do...")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
    operation = input("Enter choice( 1 / 2 / 3 / 4 ): ")

    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operation == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operation == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operation == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        continuequestion = input("Continue? (yes/no): ")
        if lower(continuequestion) == "no":
          break
    
    else:
        print("Invalid Input")
