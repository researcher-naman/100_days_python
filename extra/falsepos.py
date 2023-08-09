# Python program to find the roots by False Position Method

from ast import Break


print("FALSE POSITION METHOD\n")

# Making equtaion

def maineqx(x):
    return x*x*x - x - 1

# Asking user to assing the range

a = int(input("Enter The -ve Number: ")) # taking -ve number
b = int(input("Enter The +ve Number: ")) # taking +ve number

if (maineqx(a)*maineqx(b)>0):
    print("Your data is Wrong")
    exit()
else:
    print("\n")

n = int(input("Enter the Itration you have to find : ")) # Asking user how many time itration is to be done
    
    
def false_pos(a,b):
    
    # STEP 1 for sloving the formula and find the value of c
    
    half_1 = b-a 
    
    half_2 = maineqx(b) - maineqx(a)
    
    half_12 = half_1 / half_2
    
    half_3 = maineqx(a) * half_12
    
    c = a - half_3
    
    print("We calculated value of c form c = a - {f(b) * [b-a / f(b)-f(a)]}")
    print("And we got c as: " + str(c))    
    
    # STEP 2 now finding f(c)
    
    c_value = maineqx(c)
    print("So the value of f(" + str(c) + ") is " + str(c_value))
    
    # STEP 3 see and of c_value for -ve and +ve for changeing a or b
    
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
    a,b = false_pos(a,b)
    print("-------------------------------------")
    
print("\nSo the final root for this funtion is " + str(a) + " or " + str(b))
    
    