def operation(n1,b,n2):
    if (b=='+'):
        t = n1+n2
    if (b == '-'):
        t = n1 - n2
    if (b == '*'):
        t = n1*n2
    if ( b== '/'):
        t = n1/n2
    return(t)
print(" + for addition, - for subtraction, * for multiplication, / for division")
n1 = int(input("Enter the 1st no"))
n2 = int(input("Enter the 2nd no"))
b = input("Enter operation:")
print(operation(n1,b,n2))