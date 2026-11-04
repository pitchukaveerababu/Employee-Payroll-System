def calculate_salary(emp, attendance):

    basic_salary = emp.salary

    working_days = attendance["Working_days"]
    present_days = attendance["Present_days"]

    hra = basic_salary * 0.20
    da = basic_salary * 0.10
    pf = basic_salary * 0.12

    daily_salary = basic_salary / working_days

    earned_basic = daily_salary * present_days
    earned_hra = (hra / working_days) * present_days
    earned_da = (da / working_days) * present_days

    gross_salary = earned_basic + earned_hra + earned_da
    net_salary = gross_salary - pf

    return {
        "basic": round(earned_basic, 2),
        "hra": round(earned_hra, 2),
        "da": round(earned_da, 2),
        "gross": round(gross_salary, 2),
        "pf": round(pf, 2),
        "net": round(net_salary, 2)
    }