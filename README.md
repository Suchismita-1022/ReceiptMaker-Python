#  PDF Receipt Generator (Python + ReportLab)

This project generates a **professional PDF report** showing **item-wise performance details** using **Python and ReportLab**.

The PDF includes:
- Item name
- Price per item
- Quantity
- Total price per item
- Subtotal
- Discount
- Final total

OR
- Date
- Item name
- Subscription / Duration
- Total price 
- Subtotal
- Discount
- Final total

---

## 📂 Project Structure
```
project_folder/
│
├── receipt.py # Existing receipt generator 
├── receipt.pdf # Generated receipt PDF
│
├── item_performance.py # Item performance report generator
├── item_performance.pdf # Generated performance PDF
│
└── README.md
```

---

## 🛠️ Technologies Used

- Python 3
- ReportLab (PDF generation)

---

## ✅ Prerequisites

Make sure you have:

- **Python 3.7 or above**
- `pip` installed

Check Python version:
 ```bash
   python --version    
  ```
---

## 📦 Install Required Library

Install ReportLab using pip:
 ```bash
   pip install reportlab
   ```


If permission issues occur:

  ```bash
    pip install reportlab --user
  ```
---
## ▶️ How to Run the Project
### 1️⃣ Generate Receipt PDF (Existing File)
  ```bash
    python receipt.py
  ```


This creates:

 ```
  receipt.pdf
 ```

### 2️⃣ Generate Item Performance PDF (New File)
  ```bash
    python item_performance.py
  ```


**The program will ask for:**

- Number of items

- Item name

- Price per item

- Quantity

- Discount (optional)

**After execution, this file will be created:**

  ```
    item_performance.pdf
  ```

---

## 📄 Sample PDF Output

### Payment Receipt


| Date       | Subscription Name                                      | Subscription Type | Price (Rs.) |
|------------|--------------------------------------------------------|-------------------|-------------|
| 16/11/2020 | Full Stack Development with React & Node JS – Live      | Lifetime          | 10,999.00  |
| 16/11/2020 | Geeks Classes: Live Session                             | 6 Months          | 9,999.00   |
|            |                                                        | **Sub Total**     | **20,998.00** |
|            |                                                        | **Discount**      | **-3,000.00** |
|            |                                                        | **Total**         | **17,998.00** |



<img width="689" height="450" alt="image" src="https://github.com/user-attachments/assets/52af74fb-c37f-482a-998d-53be05bdf266" />


### Item Performance Report


| Item Name | Price per Item | Quantity | Total Price |
|-----------|----------------|----------|-------------|
| Pen       | 10.00          | 20       | 200.00      |
| Notebook | 50.00          | 10       | 500.00      |
|           |                | **Sub Total** | **700.00** |
|           |                | **Discount**  | **-50.00** |
|           |                | **Total**     | **650.00** |



<img width="715" height="460" alt="image" src="https://github.com/user-attachments/assets/d22130bc-fbee-4820-ac27-0706a0afbee1" />

---

## ✨ Features

- Dynamic user input

- Clean table formatting

- Automatic total calculation

- Separate PDF for reporting

- No modification to existing receipt code

---

## 🚀 Future Improvements

- Add invoice number & date

- Add company logo

- Generate both PDFs in one run

- Web UI using Flask/Django

- Store PDFs per customer

- Add charts in performance report

---

