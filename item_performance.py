from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- PDF SETUP ----------------
pdf = SimpleDocTemplate("item_performance.pdf", pagesize=A4)

styles = getSampleStyleSheet()
title_style = styles["Heading1"]
title_style.alignment = 1

title = Paragraph("Item Performance Report", title_style)

# ---------------- TABLE DATA ----------------
data = [["Item Name", "Price per Item (Rs.)", "Quantity", "Total Price (Rs.)"]]

n = int(input("Enter number of items: "))

grand_total = 0  # FIX: total of all items

for i in range(n):
    print(f"\nItem {i+1}")
    name = input("Enter item name: ")
    price = float(input("Enter price per item (Rs.): "))
    quantity = int(input("Enter quantity: "))

    total_price = price * quantity
    grand_total += total_price  # FIX

    data.append([name, f"{price:.2f}", quantity, f"{total_price:.2f}"])

# ---------------- SUMMARY ----------------
discount = float(input("\nEnter discount (Rs., 0 if none): "))
final_total = grand_total - discount

data.append(["", "", "Sub Total", f"{grand_total:.2f}"])
data.append(["", "", "Discount", f"-{discount:.2f}"])
data.append(["", "", "Total", f"{final_total:.2f}"])

# ---------------- TABLE STYLE ----------------
style = TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BACKGROUND", (0, 1), (-1, -4), colors.beige),
    ("BACKGROUND", (0, -3), (-1, -1), colors.lightgrey),
])

table = Table(data, style=style)

# ---------------- BUILD PDF ----------------
pdf.build([title, table])

print("\n✅ item_performance.pdf generated successfully")
