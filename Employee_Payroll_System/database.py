import mysql.connector
from getpass import getpass


DB_PASSWORD = getpass("Enter MySQL password: ")

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=DB_PASSWORD,
            database="employee_payroll"
        )

        if connection.is_connected():
            print("MySQL Database Connected Successfully!")

        return connection

    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None


def insert_employee(emp):

    connection = connect_db()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO employees (emp_id, emp_name, department, salary)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        emp.emp_id,
        emp.emp_name,
        emp.department,
        emp.salary
    )

    try:
        cursor.execute(query, values)
        connection.commit()

        print("Employee saved to database successfully!")
        return True

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        connection.close()
def get_all_employees():

    connection = connect_db()

    if connection is None:
        return []

    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM employees")

        records = cursor.fetchall()

        return records

    except mysql.connector.Error as err:
        print("Error:", err)
        return []

    finally:
        cursor.close()
        connection.close()
def get_employee(emp_id):

    connection = connect_db()

    if connection is None:
        return None

    cursor = connection.cursor()

    try:
        query = "SELECT * FROM employees WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))

        record = cursor.fetchone()

        return record

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        connection.close()
def update_employee_db(emp):

    connection = connect_db()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    UPDATE employees
    SET emp_name = %s,
        department = %s,
        salary = %s
    WHERE emp_id = %s
    """

    values = (
        emp.emp_name,
        emp.department,
        emp.salary,
        emp.emp_id
    )

    try:
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee updated in database!")
            return True

        print("No changes made.")
        return False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        connection.close()
def delete_employee_db(emp_id):
    connection = connect_db()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        query = "DELETE FROM employees WHERE emp_id = %s"
        cursor.execute(query, (emp_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print("Employee deleted from database!")
            return True

        return False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        connection.close()
def insert_attendance(emp_id, working_days, present_days, attendance_month):

    connection = connect_db()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO attendance
        (emp_id, working_days, present_days, attendance_month)
        VALUES (%s, %s, %s, %s)
        """

        values = (
            emp_id,
            working_days,
            present_days,
            attendance_month
        )

        cursor.execute(query, values)
        connection.commit()

        print("Attendance saved successfully!")
        return True

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        connection.close()
def get_attendance(emp_id, attendance_month):

    connection = connect_db()

    if connection is None:
        return None

    cursor = connection.cursor()

    try:
        query = """
        SELECT working_days, present_days
        FROM attendance
        WHERE emp_id = %s AND attendance_month = %s
        """

        cursor.execute(query, (emp_id, attendance_month))
        record = cursor.fetchone()

        if record:
            return {
                "Working_days": record[0],
                "Present_days": record[1]
            }

        return None

    except mysql.connector.Error as err:
        print("Error:", err)
        return None

    finally:
        cursor.close()
        connection.close()
def update_attendance(emp_id, working_days, present_days, attendance_month):

    connection = connect_db()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:
        query = """
        UPDATE attendance
        SET working_days = %s,
            present_days = %s
        WHERE emp_id = %s
        AND attendance_month = %s
        """

        values = (
            working_days,
            present_days,
            emp_id,
            attendance_month
        )

        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            print("Attendance updated successfully!")
            return True

        print("Attendance record not found!")
        return False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    connection = connect_db()

    if connection:
        connection.close()
        print("Database connection closed.")