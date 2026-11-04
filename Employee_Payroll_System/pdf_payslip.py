
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.units import mm


def generate_pdf_payslip(emp, attendance, salary_details, attendance_month):

    os.makedirs("Payslips", exist_ok=True)

    file_name = f"Payslips/Payslip_{emp.emp_id}_{attendance_month[:7]}.pdf"

    pdf = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=20,
        textColor=colors.HexColor("#17365D"),
        alignment=TA_CENTER,
        spaceAfter=8
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=12,
        textColor=colors.HexColor("#17365D"),
        spaceBefore=10,
        spaceAfter=7
    )

    elements = []

    # Company header
    elements.append(Paragraph("EMPLOYEE PAYROLL SYSTEM", title_style))
    elements.append(
        Paragraph(
            "MONTHLY SALARY SLIP",
            ParagraphStyle(
                "Subtitle",
                parent=styles["Normal"],
                alignment=TA_CENTER,
                fontSize=11
            )
        )
    )

    elements.append(Spacer(1, 12))

    # Payslip information
    elements.append(Paragraph("Payslip Information", heading_style))

    info_data = [
        ["Payslip Month", attendance_month[:7],
         "Generated On", datetime.now().strftime("%d-%m-%Y")],
        ["Employee ID", str(emp.emp_id),
         "Department", str(emp.department)]
    ]

    info_table = Table(info_data, colWidths=[32*mm, 50*mm, 32*mm, 45*mm])

    info_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#DCE6F1")),
        ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#DCE6F1")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTNAME", (2, 0), (2, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))

    elements.append(info_table)

    # Employee details
    elements.append(Paragraph("Employee Details", heading_style))

    employee_data = [
        ["Employee Name", str(emp.emp_name)],
        ["Employee ID", str(emp.emp_id)],
        ["Department", str(emp.department)]
    ]

    employee_table = Table(employee_data, colWidths=[55*mm, 104*mm])

    employee_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#DCE6F1")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))

    elements.append(employee_table)

    # Attendance details
    working_days = attendance["Working_days"]
    present_days = attendance["Present_days"]
    absent_days = working_days - present_days

    elements.append(Paragraph("Attendance Summary", heading_style))

    attendance_data = [
        ["Working Days", "Present Days", "Absent Days"],
        [str(working_days), str(present_days), str(absent_days)]
    ]

    attendance_table = Table(
        attendance_data,
        colWidths=[53*mm, 53*mm, 53*mm]
    )

    attendance_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("PADDING", (0, 0), (-1, -1), 9)
    ]))

    elements.append(attendance_table)

    # Salary details
    elements.append(Paragraph("Salary Breakdown", heading_style))

    salary_data = [
        ["Description", "Amount (INR)"],
        ["Basic Salary", f"Rs. {salary_details['basic']:,.2f}"],
        ["House Rent Allowance (HRA)", f"Rs. {salary_details['hra']:,.2f}"],
        ["Dearness Allowance (DA)", f"Rs. {salary_details['da']:,.2f}"],
        ["Gross Salary", f"Rs. {salary_details['gross']:,.2f}"],
        ["Provident Fund (PF) Deduction", f"Rs. {salary_details['pf']:,.2f}"]
    ]

    salary_table = Table(salary_data, colWidths=[105*mm, 54*mm])

    salary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 4), (-1, 4), colors.HexColor("#E2F0D9")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 4), (-1, 4), "Helvetica-Bold"),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("PADDING", (0, 0), (-1, -1), 9)
    ]))

    elements.append(salary_table)
    elements.append(Spacer(1, 15))

    # Net salary highlight
    net_data = [
        ["NET SALARY PAYABLE", f"Rs. {salary_details['net']:,.2f}"]
    ]

    net_table = Table(net_data, colWidths=[105*mm, 54*mm])

    net_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#17365D")),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("PADDING", (0, 0), (-1, -1), 12)
    ]))

    elements.append(net_table)
    elements.append(Spacer(1, 25))

    elements.append(
        Paragraph(
            "This is a computer-generated payslip.",
            ParagraphStyle(
                "Footer",
                parent=styles["Normal"],
                alignment=TA_CENTER,
                fontSize=8,
                textColor=colors.grey
            )
        )
    )

    pdf.build(elements)

    print("Professional PDF Payslip generated successfully!")
    print("File Name:", file_name)
