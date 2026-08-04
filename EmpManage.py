Employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Employee Salary: "))

    employee = {
        "ID": emp_id,
        "NAME": emp_name,
        "SALARY": emp_salary
    }

    Employees.append(employee)
    print("Employee added successfully!")

def view_employee():
    if not Employees:
        print("No employees found")
    else:
        for emp in Employees:
            print(emp)

def search_employees():
    emp_id = input("Enter Employee ID to search: ")

    for emp in Employees:
        if emp["ID"] == emp_id:
            print("Employee found:", emp)
            return

    print("Employee not found")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")

    for emp in Employees:
        if emp["ID"] == emp_id:
            emp["NAME"] = input("Enter new name: ")
            emp["SALARY"] = float(input("Enter new salary: "))
            print("Employee updated successfully!")
            return

    print("Employee not found")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")

    for emp in Employees:
        if emp["ID"] == emp_id:
            Employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found")


# MENU
while True:
    print("\n===== Employee Database =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        search_employees()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Program ended")
        break
    else:
        print("Invalid choice")