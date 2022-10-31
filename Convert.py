def First_Number_Convert_To_Binary(num1):   #Function for converting First decimal value to the binary
    rem=0
    List=[]                                 # Declaring empty list.
    reverse_List=[]
    while (num1 != 1):
        rem=num1%2
        num1=num1//2
        List.append(rem)                    # It will add the rem. to the list form index 0
    List.append(num1)                       # It will add the last num to the list at the last index.
    x=(len(List)-1)                         # It will calcuate size of the list and subtract 1 from the size.
    while x>=0:
        reverse_List.append(List[x])        # Reversing the list.
        x=x-1                               # Decreasing the value of 'x'
    d=8-len(reverse_List)
    for i in range (d):
        reverse_List.insert(0 ,0)        # Inserting the 0 value.
    return reverse_List


def Second_Number_Convert_To_Binary(num2):    #Function for converting Second decimal value to the binary.
    rem=0
    List=[]
    reverse_List=[]
    while (num2 != 1):
        rem=num2%2
        num2=num2//2
        List.append(rem)
    List.append(num2)
    x=(len(List)-1)
    while x>=0:
        reverse_List.append(List[x])
        x=x-1
    d=8-len(reverse_List)
    for i in range (d):
        reverse_List.insert(0,0)
    return reverse_List

