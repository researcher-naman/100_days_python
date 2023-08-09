# Python program to find the roots by Itrative / Bisection method

print("BISECTION METHOD\n")

# Making equtaion

def maineqx(x):
    return x*x*x*x - x*x*x - x*x -4

# Asking user to assing the range

a = int(input("Enter The -ve Number: ")) # taking -ve number
b = int(input("Enter The +ve Number: ")) # taking +ve number
n = int(input("Enter the Itration you have to find : ")) # Asking user how many time itration is to be done

def bisection(a,b):
    # Step 1st
    c = (a+b)/2
    print("\na+b/2 = " + str(a) + "+" + str(b) + "/2 = " + str(c))
    
    # Step 2nd
    c_value = maineqx(c)
    print("So the value of f(" + str(c) + ") is " + str(c_value))
    
    # Step 3rd
    if (c_value < 0):
        print("Which is -ve")
        a = c
        b = b
        print("now new value of a is " + str(a))
    else:
        print("Which is +ve")
        b = c
        a = a
        print("now new value of b is " + str(b))
    return (a,b)

for i in range(1, n+1):
    print("\nItration Number:" + str(i) + "\n")
    print("-------------------------------------")
    a,b = bisection(a,b)
    print("-------------------------------------")
    
print("\nSo the final root for this funtion is " + str(a) + " or " + str(b))