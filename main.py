import Number_Input
import Binary_Addition
import Convert
choice ='yes'
while(choice != 'no'):
    if(choice == 'yes'):

        loop_for_first_number=True
        while loop_for_first_number !=False:
            try:
                first=int(input("Enter the first number between 0-255: ")) 
                a=Number_Input.first_number(first)                         
                loop_for_first_number=False

            except:
                print("Enter integer only.")
                loop_for_first_number=True

        loop_for_second_number=True
        while loop_for_second_number !=False:
            try:
                second=int(input("Enter the second number between 0-255: ")) 
                b=Number_Input.second_number(second)                         
                loop_for_second_number=False
                
            except:
                print("Enter integer only.")
                loop_for_second_number=True


        print("First Number: "+str(a))          # printing the first number.
        print("Second Number: "+str(b))         # printing the second number.

        #----------||Passing the value of First number to First_Number_Convert_To_Binary function||----------#
        q=Convert.First_Number_Convert_To_Binary(a)     # converting first number to the binary and assigning in list.           
        w=[str(index) for index in q]                   # convreing the binary list to the string.
        e=''.join(w)                                    # joining the string.
        print("First number in binary: "+e)             # printing the value.

        #---------||Passing the value of Second number to Second_Number_Convert_To_Binary function||---------#                
        r=Convert.Second_Number_Convert_To_Binary(b)    # converting second number to the binary and assigning in list.
        t=[str(index) for index in r]                   # convreing the binary list to the string.
        y=''.join(t)                                    # joining the string.
        print("Second number in binary: "+y)            # printing the value.

        #---------||Passing the value of q and r in the format oflist to Binary_Addition function||---------#
        c=Binary_Addition.Binary_add(q,r)               # assigning the valur of the q and r to the function of binary addition
        m=[str(index) for index in c]                   # converting the binary list to the string.
        n=''.join(m)                                    # joining the string.
        print("Sum of numbers in binary: "+str(n))      # printing the sum of two binary number.

        #---------||Passing the value inputted by the user to Binary_Addition function||---------#
        x=Binary_Addition.decimal_addition(a,b)         # Passing the values.
        print("Sum of numbers in decimal: "+str(x))     # printing the value of two decimal number.
    else:
        print("Enter yes or no.")
    choice=input("Do you want to continue?yes or no: ")  # asking user to continue or not.
