from validation import get_integer, get_positive_float, get_non_empty_string
from employee import Employee
from attendance import mark_attendance, view_attendance, modify_attendance
from payroll import calculate_salary
from payslip import generate_payslips
from database import (
    insert_employee,
    get_all_employees,
    get_employee,
    update_employee_db,
    delete_employee_db,
    get_attendance
)
from pdf_payslip import generate_pdf_payslip
def add_employee():

    emp_id = get_integer("Enter Employee ID: ")

    emp_name = get_non_empty_string("Enter Employee Name: ")

    department = get_non_empty_string("Enter Department: ")

    salary = get_positive_float("Enter Salary: ")

    emp = Employee(emp_id, emp_name, department, salary)

    if insert_employee(emp):
        print("Employee added successfully!")
def view_employees():

    records = get_all_employees()

    if not records:
        print("No employee found!")
        return

    for emp in records:
        print("Employee ID:", emp[0])
        print("Employee Name:", emp[1])
        print("Department:", emp[2])
        print("Salary:", emp[3])
        print("----------------------")
def search_employee():

    search_id = get_integer("Enter Employee ID: ")

    record = get_employee(search_id)

    if record is None:
        print("Employee not found!")
        return None

    emp = Employee(
        record[0],
        record[1],
        record[2],
        float(record[3])
    )

    print("Employee Found!")
    emp.display_employee()

    return emp
def update_employee():

    emp = search_employee()

    if emp is None:
        return

    print("1. Update Name")
    print("2. Update Department")
    print("3. Update Salary")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp.emp_name = get_non_empty_string("Enter New Name: ")

    elif choice == "2":
        emp.department = get_non_empty_string("Enter New Department: ")
    elif choice == "3":
        emp.salary = get_positive_float("Enter New Salary: ")
    else:
        print("Invalid Choice!")
        return

    if update_employee_db(emp):
        emp.display_employee()  
def delete_employee():
    emp = search_employee()

    if emp is None:
        return
    confirm = input("Are you sure you want to delete? (yes/no): ").strip().lower()

    if confirm == "yes":
        if delete_employee_db(emp.emp_id):
            print("Employee deleted successfully!")
    elif confirm == "no":
        print("Deletion cancelled!")
    else:
        print("Invalid choice! Enter yes or no.")
def generate_payroll():

    emp = search_employee()

    if emp is None:
        return

    attendance_month = input("Enter Attendance Month (YYYY-MM): ")

    try:
        year, month = map(int, attendance_month.split("-"))

        if not (2000 <= year and 1 <= month <= 12):
            print("Invalid month!")
            return

        attendance_month = f"{year:04d}-{month:02d}-01"

    except ValueError:
        print("Invalid format! Use YYYY-MM.")
        return

    attendance_record = get_attendance(emp.emp_id, attendance_month)

    if attendance_record is None:
        print("Attendance not found for this month!")
        return

    salary_details = calculate_salary(emp, attendance_record)

    print("Gross Salary:", salary_details["gross"])
    print("PF Deduction:", salary_details["pf"])
    print("Net Salary:", salary_details["net"])
def generate_employee_payslip():

    emp = search_employee()

    if emp is None:
        return

    attendance_month = input("Enter Attendance Month (YYYY-MM): ")

    try:
        year, month = map(int, attendance_month.split("-"))

        if not (2000 <= year and 1 <= month <= 12):
            print("Invalid month!")
            return

        attendance_month = f"{year:04d}-{month:02d}-01"

    except ValueError:
        print("Invalid format! Use YYYY-MM.")
        return

    attendance_record = get_attendance(emp.emp_id, attendance_month)

    if attendance_record is None:
        print("Attendance not found for this month!")
        return

    salary_details = calculate_salary(emp, attendance_record)

    generate_payslips(emp, attendance_record)

    generate_pdf_payslip(
    emp,
    attendance_record,
    salary_details,
    attendance_month
    )
def main():

    while True:

        print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search for employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Mark Attendance")
        print("7. View Attendance")
        print("8. Generate Payroll")
        print("9. Generate payslip")
        print("10. Update Attendance")
        print("11. Exit")


        choice = input("Enter your choice: ")
        if choice=="1":
            add_employee()
        elif choice=="2":
            view_employees()
        elif choice=="3":
            search_employee()
        elif  choice=="4":
            update_employee()
        elif choice=="5":
            delete_employee()
        elif choice=="6":
            mark_attendance()
        elif choice =="7":
            view_attendance()
        elif choice=="8":
            generate_payroll()
        elif choice=="9":
            generate_employee_payslip()
        elif choice=="10":
            modify_attendance()
        
        elif choice=="11":
            print("Thank u for using Employee payroll sysytem!")
            break
        else:
            print("Invalid choice! Please try again.")
main()

