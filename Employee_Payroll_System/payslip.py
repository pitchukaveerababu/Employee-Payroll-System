from payroll import calculate_salary
def generate_payslips(emp, attendance):

    salary_details = calculate_salary(emp, attendance)

    if salary_details is None:
        print("Payslip generation failed!")
        return
    working_days=attendance["Working_days"]
    present_days=attendance["Present_days"]
    absent_days=working_days-present_days
    print("\n============================")
    print("         Employee Payslip")
    print("==============================")
    print("Employee ID:",emp.emp_id)
    print("Employee Name:",emp.emp_name)
    print("Department:",emp.department)
    print("------------------------------")
    print("         Attendance Details")
    print("------------------------------")
    print("Working Days:",working_days)
    print("Present Days:",present_days)
    print("Absent Days:",absent_days)
    print("------------------------------")
    print("         Salary Details")
    print("------------------------------")
    print("Basic Salary:", salary_details["basic"])
    print("HRA:", salary_details["hra"])
    print("DA:", salary_details["da"])
    print("Gross Salary:", salary_details["gross"])
    print("PF Deduction:", salary_details["pf"])
    print("==============================")
    print("Net Salary:",salary_details["net"])
    print("==============================")
