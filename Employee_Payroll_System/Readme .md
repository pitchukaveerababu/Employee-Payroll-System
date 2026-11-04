# Employee Payroll Management System

A Python-based Employee Payroll Management System that uses MySQL for data storage and ReportLab for generating professional PDF payslips. The application provides employee management, monthly attendance tracking, salary calculation, and payslip generation through a menu-driven interface.

## Features

- **Employee Management (CRUD)**
  - Add new employees
  - View all employees
  - Search employees by ID
  - Update employee details
  - Delete employee records

- **Attendance Management**
  - Record monthly employee attendance
  - View attendance details
  - Update existing attendance records
  - Prevent duplicate attendance records for the same employee and month
  - Calculate absent days automatically

- **Payroll Management**
  - Calculate salary based on attendance
  - Calculate HRA and DA allowances
  - Calculate PF deductions
  - Generate gross salary and net salary

- **Payslip Generation**
  - Display payslips in the terminal
  - Generate formatted PDF payslips
  - Automatically organize generated payslips in a folder

- **Input Validation**
  - Validate employee IDs and salary inputs
  - Handle invalid numeric inputs
  - Validate attendance values and months
  - Prevent empty employee details

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| MySQL | Database management |
| MySQL Connector | Python-MySQL connectivity |
| ReportLab | PDF payslip generation |
| VS Code | Development environment |

## Project Structure

```text
Employee_Payroll_System/
│
├── main.py
├── employee.py
├── attendance.py
├── database.py
├── payroll.py
├── payslip.py
├── pdf_payslip.py
├── validation.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Payslips/
```

## Database Setup

1. Install MySQL Server 8.0 or a compatible version.
2. Open MySQL and create the database:

```sql
CREATE DATABASE employee_payroll;
USE employee_payroll;
```

3. Create the employees table:

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
```

4. Create the attendance table:

```sql
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT NOT NULL,
    working_days INT NOT NULL,
    present_days INT NOT NULL,
    attendance_month DATE NOT NULL,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    CONSTRAINT unique_employee_month
    UNIQUE (emp_id, attendance_month)
);
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Employee_Payroll_System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure MySQL

Update the database connection settings in `database.py` to use your local MySQL configuration.

Do not commit your database password or other credentials to GitHub. Use environment variables or another secure configuration method.

### 7. Run the application

```bash
python main.py
```

## Application Menu

```text
===== EMPLOYEE PAYROLL SYSTEM =====

1. Add Employee
2. View Employees
3. Search for employee
4. Update Employee
5. Delete Employee
6. Mark Attendance
7. View Attendance
8. Generate Payroll
9. Generate Payslip
10. Update Attendance
11. Exit
```

## Salary Calculation

The application uses the following simplified training calculation:

- HRA = 20% of basic salary
- DA = 10% of basic salary
- PF = 12% of monthly basic salary
- Earned basic salary = (Basic salary / Working days) × Present days
- Earned HRA = (HRA / Working days) × Present days
- Earned DA = (DA / Working days) × Present days
- Gross salary = Earned basic + Earned HRA + Earned DA
- Net salary = Gross salary − PF

*Note: These are simplified project assumptions for demonstration and are not intended to represent statutory payroll calculations.*

## Future Enhancements

- Role-based authentication for administrators and employees
- Salary history and payroll records
- Monthly payroll reports
- Automated email delivery of payslips
- Improved dashboard and graphical user interface
- Advanced reporting and analytics

## Author

**Veera Babu**

- GitHub: https://github.com/pitchukaveerababu

## License

This project is developed for educational and portfolio purposes.