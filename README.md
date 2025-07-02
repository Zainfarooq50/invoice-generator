# AI-Powered Invoice Generator with PDF Export & Logging

This Python tool generates professional invoice PDFs, complete with tax calculations, unique invoice numbering, AI-generated summaries, and automated CSV logging. Ideal for freelancers, small businesses, or anyone needing automated invoice creation with AI-enhanced summaries.

---

## ⚡ Features
✅ Creates ready-to-send Invoice PDFs with clean formatting  
✅ Auto-increments invoice numbers for each new invoice  
✅ Tax calculation based on user-defined rate  
✅ AI-generated professional invoice summary using GPT  
✅ Automatically logs invoices to a CSV file for easy tracking  
✅ Stores invoices and logs in a structured folder  

---

## 🛠️ Requirements
- Python 3.x  
- `reportlab`, `os`, `csv`, `datetime`  
- `GPT_utils_invoice.py` with AI integration (requires OpenAI API key)  

---

## 🚀 How to Use
1. Paste your OPENAI key in .env file.
2. Run the script:  
   ```bash
   python invoice_generator.py
Enter the required details:

Client name

Service description

Amount (numeric)

Tax rate (decimal, e.g., 0.1 for 10%)

The tool will:
✅ Generate a PDF invoice with clean layout and AI-written summary
✅ Save the PDF inside the invoices folder
✅ Log invoice details to invoices/invoice_log.csv
✅ Auto-update the invoice number counter

📁 Example Output Structure
Copy
Edit
invoices/
├── Invoice_1_ClientName_20250702_153210.pdf
├── invoice_counter.txt
├── invoice_log.csv
📄 Example PDF Contents
Invoice number, client, service, amount, tax, total

AI-Generated summary explaining the invoice professionally

Clean, ready-to-share layout in PDF format

🤖 AI Integration
Model: GPT-3.5-Turbo

AI generates clear, concise invoice summaries for professional communication

Summary automatically embedded inside the PDF

💼 Ideal Use Cases
✔ Freelancers creating invoices for clients
✔ Small businesses automating invoice workflows
✔ Finance teams enhancing invoices with AI-generated descriptions
✔ Quick, professional invoice generation with minimal setup
