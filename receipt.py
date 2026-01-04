from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

# Create PDF
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1

title = Paragraph("Payment Receipt", title_style)

# Table Header (Date added)
DATA = [["Date", "Item Name", "Subscription", "Price (Rs.)"]]

total_amount = 0

# Use today's date automatically
today_date = datetime.now().strftime("%d/%m/%Y")

# Number of items
n = int(input("Enter number of items: "))

for i in range(n):
    print(f"\nItem {i+1}")
    name = input("Enter item name: ")
    subscription = input("Enter subscription/duration: ")
    price = float(input("Enter price (Rs.): "))

    total_amount += price
    DATA.append([today_date, name, subscription, f"{price:.2f}"])

# Discount
discount = float(input("\nEnter discount (Rs., 0 if none): "))
final_total = total_amount - discount

# Summary rows
DATA.append(["", "", "Sub Total", f"{total_amount:.2f}"])
DATA.append(["", "", "Discount", f"-{discount:.2f}"])
DATA.append(["", "", "Total", f"{final_total:.2f}"])

# Table Style
style = TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -4), colors.beige),
    ("BACKGROUND", (0, -3), (-1, -1), colors.lightgrey),
])

table = Table(DATA, style=style)

pdf.build([title, table])

print("\n✅ Receipt generated successfully as 'receipt.pdf'")
