# Day 14 PYTHON Programming

# IF-ELSE statements

#program to Show subject list according to there class
head = "Program to find subject list form class 6 to 10"
print(head.center(150))
print("\n")

cls = int(input("Enter your class: ")) # here "cls" means class
print("\n Subject in class " + str(cls) + "th are given below.\n")

if(cls == 5):
    print("English\n")
    print("Hindi\n")
    print("Environmental Science\n")
    print("Computer\n")
    print("Maths\n")
elif(cls == 6):
    print("English\n")
    print("Hindi\n")
    print("Science\n")
    print("Social Science\n")
    print("Maths\n")
elif(cls == 7):
    print("English\n")
    print("Hindi\n")
    print("Science\n")
    print("Social Science\n")
    print("Maths\n")
    print("Computer\n")
elif(cls == 8):
    print("English\n")
    print("Hindi\n")
    print("Science\n")
    print("Social Science\n")
    print("Maths\n")
    print("Computer\n")
elif(cls == 9):
    print("English\n")
    print("Hindi\n")
    print("Science\n")
    print("Social Science\n")
    print("Maths\n")
    print("Computer\n")
    print("Economics\n")
elif(cls == 10):
    print("English\n")
    print("Hindi\n")
    print("Physics\n")
    print("Chemistry\n")
    print("Biology\n")
    print("Social Science\n")
    print("Maths\n")
    print("Computer\n")
else:
    print("Sorry we can't find the subject list for given class.")