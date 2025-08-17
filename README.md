# PDF to TXT Converter (Python – pdfplumber)

This Python script converts one or more PDF files into `.txt` files using the **pdfplumber** library.  
It provides more accurate text extraction than PyPDF2, especially for PDFs with structured layouts.

---

## 📌 Features
- Extracts text from PDFs and saves them into `.txt` files.
- Handles multiple PDFs in a single run.
- Uses **pdfplumber** for precise text extraction.
- Skips empty pages automatically.
- Continuous usage: run multiple times until you type `exit`.

---

## 🛠️ Requirements
Install dependencies:

```bash
pip install pdfplumber
````

---

## 🚀 Usage

Run the script:

```bash
python pdf_to_txt_plumber.py
```

Example flow:

```
Press Y to use or type 'exit' to quit: y
Enter the number of PDFs you want to work on: 2
Enter the PDF file name no.1: sample1.pdf
Enter the PDF file name no.2: sample2.pdf
✅ Conversion done: word_sample1.txt
✅ Conversion done: word_sample2.txt
Press Y to use or type 'exit' to quit: exit
Exiting program...
```

---

## 📂 Example Project Structure

```
├── pdf_to_txt_plumber.py   # Main script
├── README.md               # Documentation
├── sample1.pdf             # Example input
└── word_sample1.txt        # Example output
```

---

## ⚠️ Notes

* Works only with **text-based PDFs**.
* For scanned/image PDFs, use OCR tools like **pytesseract**.
* Enter the correct file names or provide full paths.

---

## 📜 License

This project is open-source under the **MIT License**.

```

---
