import os
import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from datetime import datetime
from GPT_utils_invoice import generate_invoice_summary

# ---------------- Setup ----------------
os.makedirs("invoices", exist_ok=True)
invoice_counter_file = "invoices/invoice_counter.txt"

# Initialize counter if missing
if not os.path.exists(invoice_counter_file):
    with open(invoice_counter_file, "w") as f:
        f.write("1")

# Read invoice number
with open(invoice_counter_file, "r") as f:
    invoice_number = int(f.read().strip())

# ---------------- User Input ----------------
client = input("Client Name: ").strip()
service = input("Service Provided: ").strip()

try:
    amount = float(input("Amount ($): "))
    tax_rate = float(input("Tax Rate (e.g., 0.1 for 10%): "))
except ValueError:
    print("⚠️ Invalid numeric input. Exiting.")
    exit()

# ---------------- Calculations ----------------
tax = amount * tax_rate
total = amount + tax

# ---------------- Invoice Content ----------------
invoice_text = (
    f"Invoice Number: {invoice_number}\n"
    f"Client: {client}\n"
    f"Service: {service}\n"
    f"Amount: ${amount:.2f}\n"
    f"Tax ({tax_rate * 100:.1f}%): ${tax:.2f}\n"
    f"Total Due: ${total:.2f}\n"
)

# ---------------- AI Summary ----------------
ai_summary = generate_invoice_summary(invoice_text)

# ---------------- PDF Generation ----------------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
pdf_filename = f"invoices/Invoice_{invoice_number}_{client}_{timestamp}.pdf"

c = canvas.Canvas(pdf_filename, pagesize=A4)
c.setFont("Helvetica-Bold", 14)
c.drawString(50, 800, "INVOICE")

c.setFont("Helvetica", 12)
c.drawString(50, 770, f"Invoice Number: {invoice_number}")
c.drawString(50, 750, f"Client: {client}")
c.drawString(50, 730, f"Service: {service}")
c.drawString(50, 710, f"Amount: ${amount:.2f}")
c.drawString(50, 690, f"Tax ({tax_rate * 100:.1f}%): ${tax:.2f}")
c.drawString(50, 670, f"Total Due: ${total:.2f}")

# AI Summary with wrapping
y_position = 630
c.drawString(50, y_position, "AI-Generated Summary:")
y_position -= 20

wrapped_lines = simpleSplit(ai_summary, "Helvetica", 12, 500)
for line in wrapped_lines:
    if y_position < 100:
        break  # Prevent overflow
    c.drawString(50, y_position, line.strip())
    y_position -= 20

c.save()
print(f"✅ Invoice PDF generated: {pdf_filename}")

# ---------------- Invoice Counter Update ----------------
with open(invoice_counter_file, "w") as f:
    f.write(str(invoice_number + 1))

# ---------------- CSV Logging ----------------
log_file = "invoices/invoice_log.csv"
file_exists = os.path.isfile(log_file)

log_data = [
    invoice_number,
    client,
    service,
    f"{amount:.2f}",
    f"{tax:.2f}",
    f"{total:.2f}",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
]

with open(log_file, "a", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    if not file_exists:
        writer.writerow(["Invoice No.", "Client", "Service", "Amount", "Tax", "Total", "Date"])
    writer.writerow(log_data)

print(f"✅ Invoice logged to '{log_file}'")
