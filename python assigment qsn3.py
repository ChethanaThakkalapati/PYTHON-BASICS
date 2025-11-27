'''You’re building a small program for a school. The user must enter the student’s name and marks in three subjects. The program should calculate the total, average, and display a grade. If marks are not between 0 and 100, show an error message. 
Concepts: Input/Output, data validation, arithmetic, if–elif–else.'''

# Student grade calculator program
name = input("Enter student's name: ")


m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))


if((m1<=0 or m1>100) or (m2<=0 or m2>100) or (m3<=0 or m3>100)):
    print("Error: Marks must be between 0 and 100!")
else:
    total = m1 + m2 + m3
    average = total / 3

    
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"


    print(" Student Report")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)


