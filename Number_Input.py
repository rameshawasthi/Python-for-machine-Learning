def first_number(a):          # Function for first number
    while(a<0 or a>255):      # Condition checking
        print("Please enter a number within range (0-255)")
        a=int(input("Enter the first number between 0-255: "))
    return a                  # Returning values


def second_number(b):          # Function for second number
    while(b<0 or b>255):
        print("Please enter a number within range (0-255)")
        b=int(input("Enter the second number between 0-255: "))
    return b                   # Returning values


