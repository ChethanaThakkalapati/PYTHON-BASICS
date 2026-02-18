'''	A company needs a program that reads employee names and their basic salary.
The program should: Calculate total salary including HRA (20%) and DA (10%).
Stop taking input when the user types "stop". Display each employee’s total salary at the end.
Concepts: while loop, arithmetic operations, condition check, formatted output.'''


employees = {}   

while True:
    name = input("Enter employee name (or type 'stop' to end): ")

    if name.lower() == "stop":
        break

    
    salary = int(input(f"Enter basic salary for {name}: "))

    
    hra = int(salary * 0.20)
    da = int(salary * 0.10)
    total = salary + hra + da

    
    employees[name] = total

print(" Employee Salary Details ")
for name, total in employees.items():
    print(f"{name}: Total Salary = ₹{total:}")

