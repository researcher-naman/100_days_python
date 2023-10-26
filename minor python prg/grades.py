marks = float(input("Enter the student's marks: "))

if 80 <= marks <= 90:
    grade = "1st Grade"
elif 60 <= marks < 80:
    grade = "2nd Grade"
elif 40 <= marks < 60:
    grade = "3rd Grade"
else:
    grade = "Fail"
    
print("The student's grade is: " + str(grade))
