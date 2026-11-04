# Employee Payroll Management System

A Python-based Employee Payroll Management System integrated with MySQL to manage employee records, attendance, salary calculations, and payslip generation.

## 🚀 Project Overview

The Employee Payroll Management System simplifies payroll operations by providing employee management, attendance tracking, salary processing, and PDF payslip generation.

The application uses Python for backend logic and MySQL for database management.

## ✨ Features

- **Employee Management:** Add, view, update, and delete employee records.
- **Attendance Management:** Record and manage employee attendance.
- **Payroll Processing:** Calculate employee salaries based on attendance.
- **Payslip Generation:** Generate PDF payslips for employees.
- **Data Validation:** Validate employee details and input data.
- **Database Integration:** Store and retrieve employee and payroll information using MySQL.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend development |
| MySQL | Database management |
| MySQL Connector | Python-MySQL connectivity |
| PDF Generation | Payslip generation |

## 📂 Project Structure

```text
Employee-Payroll-System/
│
├── Employee_Payroll_System/
│   ├── attendance.py
│   ├── database.py
│   ├── employee.py
│   ├── main.py
│   ├── payroll.py
│   ├── payslip.py
│   ├── pdf_payslip.py
│   ├── validation.py
│   └── README.md
│
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/pitchukaveerababu/Employee-Payroll-System.git
```

### 2. Navigate to the project directory

```bash
cd Employee-Payroll-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install mysql-connector-python
```

Install any additional libraries required by your project.

### 6. Configure MySQL

- Install and start MySQL Server.
- Create a database named `employee_payroll`.
- Create the required employee and attendance tables.
- Configure your MySQL username and password.

### 7. Run the application

```bash
cd Employee_Payroll_System
python main.py
```

Enter your MySQL password when prompted.

## 🗄️ Database

MySQL is used to store and manage:

- Employee details
- Attendance records
- Salary information
- Payroll data

## 🎯 Learning Outcomes

- Python application development.
- MySQL database connectivity.
- CRUD operations.
- SQL queries and database transactions.
- Payroll calculation logic.
- Input validation and exception handling.
- PDF generation.

## 👨‍💻 Author

**Pitchuka Veerababu**

GitHub: https://github.com/pitchukaveerababu

---

Developed as a Python and MySQL project to demonstrate practical software development and database management skills.
