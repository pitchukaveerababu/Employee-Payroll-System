
from database import (
    insert_attendance,
    get_attendance,
    get_employee,
    update_attendance
)

from validation import get_integer, get_non_negative_integer


def mark_attendance():

    emp_id = get_integer("Enter Employee ID: ")

    emp = get_employee(emp_id)

    if emp is None:
        print("Employee ID not found!")
        return

    attendance_month = input("Enter Attendance Month (YYYY-MM): ").strip()

    try:
        year, month = map(int, attendance_month.split("-"))

        if year < 2000 or not 1 <= month <= 12:
            print("Invalid month!")
            return

        attendance_month = f"{year:04d}-{month:02d}-01"

    except ValueError:
        print("Invalid format! Use YYYY-MM.")
        return

    working_days = get_integer("Enter Total Working Days: ")
    present_days = get_non_negative_integer("Enter Present Days: ")

    if present_days > working_days:
        print("Present days cannot exceed working days!")
        return

    insert_attendance(
        emp_id,
        working_days,
        present_days,
        attendance_month
    )


def view_attendance():

    emp_id = get_integer("Enter Employee ID: ")

    emp = get_employee(emp_id)

    if emp is None:
        print("Employee ID not found!")
        return

    attendance_month = input("Enter Attendance Month (YYYY-MM): ").strip()

    try:
        year, month = map(int, attendance_month.split("-"))

        if year < 2000 or not 1 <= month <= 12:
            print("Invalid month!")
            return

        attendance_month = f"{year:04d}-{month:02d}-01"

    except ValueError:
        print("Invalid format! Use YYYY-MM.")
        return

    record = get_attendance(emp_id, attendance_month)

    if record is None:
        print("Attendance not found!")
        return

    working_days = record["Working_days"]
    present_days = record["Present_days"]

    print("\n===== ATTENDANCE DETAILS =====")
    print("Employee ID:", emp_id)
    print("Attendance Month:", attendance_month[:7])
    print("Working Days:", working_days)
    print("Present Days:", present_days)
    print("Absent Days:", working_days - present_days)


def modify_attendance():

    emp_id = get_integer("Enter Employee ID: ")

    emp = get_employee(emp_id)

    if emp is None:
        print("Employee not found!")
        return

    attendance_month = input("Enter Attendance Month (YYYY-MM): ").strip()

    try:
        year, month = map(int, attendance_month.split("-"))

        if year < 2000 or not 1 <= month <= 12:
            print("Invalid month!")
            return

        attendance_month = f"{year:04d}-{month:02d}-01"

    except ValueError:
        print("Invalid format! Use YYYY-MM.")
        return

    record = get_attendance(emp_id, attendance_month)

    if record is None:
        print("Attendance record not found!")
        return

    print("\n===== CURRENT ATTENDANCE =====")
    print("Working Days:", record["Working_days"])
    print("Present Days:", record["Present_days"])

    working_days = get_integer("Enter Updated Working Days: ")
    present_days = get_non_negative_integer("Enter Updated Present Days: ")

    if present_days > working_days:
        print("Present days cannot exceed working days!")
        return

    if update_attendance(
        emp_id,
        working_days,
        present_days,
        attendance_month
    ):
        print("Attendance updated successfully!")
    else:
        print("Attendance update failed!")
