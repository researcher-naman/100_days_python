# Python program to find the roots by Newton Raypson Method

print("NEWTON RAYPSON METHOD\n")

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
    
    