def Binary_add(a,b):
    carry=0
    addition=[]
    position=(len(a)-1)
    while position>=0:             # Condition checking 
        x=a[position]
        y=b[position]
        x1=x^y
        Sum=x1^carry
        a1=x&y
        a2=x1&carry
        carry=a1|a2
        addition.insert(0,Sum)
        position=position-1         # Decreasing the value of position
    if(carry==1):
        print("Sum exceeds 8 bits, 9th bit is necessary to represent sum.")
        addition.insert(0,1)
    else:
        pass
    return addition                   # Returning the value.

def decimal_addition(a,b):
    return a+b
